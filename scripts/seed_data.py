import os
import sys

try:
    from neo4j import GraphDatabase
except ImportError:
    print("Yeu cau cai dat neo4j: pip install neo4j")
    sys.exit(1)

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "antiscam_neo4j_pass")

def seed_neo4j():
    try:
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        with driver.session() as session:
            session.run("""
                CREATE CONSTRAINT unique_phone IF NOT EXISTS
                FOR (p:PhoneNumber) REQUIRE p.phone IS UNIQUE;
            """)
            session.run("""
                CREATE CONSTRAINT unique_bank_account IF NOT EXISTS
                FOR (b:BankAccount) REQUIRE (b.account_number, b.bank_bin) IS UNIQUE;
            """)
            session.run("""
                CREATE CONSTRAINT unique_social IF NOT EXISTS
                FOR (s:SocialProfile) REQUIRE s.profile_id IS UNIQUE;
            """)
            session.run("""
                CREATE CONSTRAINT unique_report IF NOT EXISTS
                FOR (r:ScamReport) REQUIRE r.report_id IS UNIQUE;
            """)

            session.run("MATCH (n) WHERE n.test_data = true DETACH DELETE n")

            query = """
            CREATE (b1:BankAccount {
                account_number: '1029384756',
                bank_bin: '970415',
                bank_name: 'VietinBank',
                account_name: 'NGUYEN VAN LUA DAO',
                test_data: true
            })
            CREATE (b2:BankAccount {
                account_number: '0987654321001',
                bank_bin: '970436',
                bank_name: 'Vietcombank',
                account_name: 'TRAN VAN RUA TIEN',
                test_data: true
            })
            CREATE (p1:PhoneNumber {
                phone: '0987654321',
                carrier: 'Viettel',
                risk_score: 95.0,
                test_data: true
            })
            CREATE (p2:PhoneNumber {
                phone: '0912999888',
                carrier: 'Vinaphone',
                risk_score: 80.0,
                test_data: true
            })
            CREATE (s1:SocialProfile {
                profile_id: 'fb_phongtro_giare_q5',
                platform: 'Facebook',
                profile_name: 'Phong Tro Gia Re Q5',
                profile_url: 'https://facebook.com/phongtro_giare_q5',
                test_data: true
            })
            CREATE (s2:SocialProfile {
                profile_id: 'zalo_0987654321',
                platform: 'Zalo',
                profile_name: 'Chu Tro Hoang Anh',
                test_data: true
            })
            CREATE (r1:ScamReport {
                report_id: 'rep_demo_001',
                incident_type: 'DEPOSIT_SCAM',
                title: 'Lua coc phong tro',
                is_verified: true,
                created_at: '2026-11-01T10:00:00Z',
                test_data: true
            })
            CREATE (img1:ImagePhash {
                hash_value: 'a3b2c1d4e5f60718',
                test_data: true
            })

            CREATE (s1)-[:USES_ACCOUNT]->(b1)
            CREATE (s2)-[:USES_ACCOUNT]->(b1)
            CREATE (s1)-[:USES_PHONE]->(p1)
            CREATE (p1)-[:USED_TO_RECEIVE]->(b1)
            CREATE (p1)-[:SHARED_CONTACT]->(p2)
            CREATE (p2)-[:USED_TO_RECEIVE]->(b2)
            CREATE (r1)-[:TARGETS_ACCOUNT]->(b1)
            CREATE (r1)-[:TARGETS_PHONE]->(p1)
            CREATE (r1)-[:TARGETS_PROFILE]->(s1)
            CREATE (r1)-[:CONTAINS_IMAGE]->(img1)
            """
            session.run(query)
            print("Seed Neo4j completed.")
        driver.close()
    except Exception as e:
        print(f"Error seeding Neo4j: {e}")

if __name__ == "__main__":
    seed_neo4j()
