import os

DIR = r"c:\Users\aoe\OneDrive\Workspace\Projects\antiscam-system\docs"
ERD_PATH = os.path.join(DIR, "ERD_TongHop_ToanHeThong.xml")
RM_PATH = os.path.join(DIR, "RM_TongHop_ToanHeThong.xml")

# Table Definitions
TABLES = {
    # Column 1: Users & Family Protection (Blue)
    "users": {
        "x": 80, "y": 60, "w": 320,
        "color": "#dae8fc", "stroke": "#6c8ebf",
        "cols": [
            ("PK", "id", "UUID"),
            ("", "full_name", "VARCHAR(100)"),
            ("", "phone", "VARCHAR(20)"),
            ("", "email", "VARCHAR(100)"),
            ("", "hashed_password", "VARCHAR(255)"),
            ("", "role", "VARCHAR(20)"),
            ("", "status", "VARCHAR(20)"),
            ("", "avatar_url", "TEXT"),
            ("", "created_at", "TIMESTAMPTZ"),
            ("", "updated_at", "TIMESTAMPTZ"),
        ]
    },
    "user_devices": {
        "x": 80, "y": 360, "w": 320,
        "color": "#dae8fc", "stroke": "#6c8ebf",
        "cols": [
            ("PK", "id", "UUID"),
            ("FK", "user_id", "UUID"),
            ("", "device_uuid", "VARCHAR(100)"),
            ("", "fcm_token", "TEXT"),
            ("", "device_model", "VARCHAR(100)"),
            ("", "os_name", "VARCHAR(30)"),
            ("", "os_version", "VARCHAR(50)"),
            ("", "is_active", "BOOLEAN"),
            ("", "last_active_at", "TIMESTAMPTZ"),
            ("", "created_at", "TIMESTAMPTZ"),
        ]
    },
    "family_guardians": {
        "x": 80, "y": 660, "w": 320,
        "color": "#dae8fc", "stroke": "#6c8ebf",
        "cols": [
            ("PK", "id", "UUID"),
            ("FK", "user_id", "UUID"),
            ("FK", "guardian_id", "UUID"),
            ("", "relationship", "VARCHAR(50)"),
            ("", "is_confirmed", "BOOLEAN"),
            ("", "can_receive_sos", "BOOLEAN"),
            ("", "can_view_history", "BOOLEAN"),
            ("", "created_at", "TIMESTAMPTZ"),
        ]
    },
    "sos_alerts": {
        "x": 80, "y": 920, "w": 320,
        "color": "#dae8fc", "stroke": "#6c8ebf",
        "cols": [
            ("PK", "id", "UUID"),
            ("FK", "user_id", "UUID"),
            ("", "trigger_source", "VARCHAR(50)"),
            ("", "suspicious_value", "VARCHAR(100)"),
            ("", "risk_score", "DOUBLE PRECISION"),
            ("", "lat", "DOUBLE PRECISION"),
            ("", "lng", "DOUBLE PRECISION"),
            ("", "address", "TEXT"),
            ("", "status", "VARCHAR(30)"),
            ("", "created_at", "TIMESTAMPTZ"),
        ]
    },
    "sos_alert_recipients": {
        "x": 80, "y": 1220, "w": 320,
        "color": "#dae8fc", "stroke": "#6c8ebf",
        "cols": [
            ("PK", "id", "UUID"),
            ("FK", "alert_id", "UUID"),
            ("FK", "guardian_id", "UUID"),
            ("", "fcm_message_id", "VARCHAR(100)"),
            ("", "delivery_status", "VARCHAR(30)"),
            ("", "delivered_at", "TIMESTAMPTZ"),
            ("", "read_at", "TIMESTAMPTZ"),
        ]
    },

    # Column 2: Master Directory & Verification (Gold/Yellow & Green)
    "banks": {
        "x": 580, "y": 60, "w": 330,
        "color": "#fff2cc", "stroke": "#d6b656",
        "cols": [
            ("PK", "id", "UUID"),
            ("", "bin", "VARCHAR(10)"),
            ("", "code", "VARCHAR(20)"),
            ("", "short_name", "VARCHAR(50)"),
            ("", "name", "VARCHAR(200)"),
            ("", "logo_url", "TEXT"),
            ("", "is_napas_supported", "BOOLEAN"),
            ("", "is_active", "BOOLEAN"),
            ("", "created_at", "TIMESTAMPTZ"),
        ]
    },
    "bank_accounts": {
        "x": 580, "y": 340, "w": 330,
        "color": "#fff2cc", "stroke": "#d6b656",
        "cols": [
            ("PK", "id", "UUID"),
            ("FK", "bank_id", "UUID"),
            ("", "account_number", "VARCHAR(50)"),
            ("", "account_holder_name", "VARCHAR(150)"),
            ("", "risk_level", "VARCHAR(20)"),
            ("", "total_reports", "INT"),
            ("", "is_blacklisted", "BOOLEAN"),
            ("", "first_reported_at", "TIMESTAMPTZ"),
            ("", "last_reported_at", "TIMESTAMPTZ"),
            ("", "created_at", "TIMESTAMPTZ"),
        ]
    },
    "phone_numbers": {
        "x": 580, "y": 640, "w": 330,
        "color": "#fff2cc", "stroke": "#d6b656",
        "cols": [
            ("PK", "id", "UUID"),
            ("", "phone_number", "VARCHAR(20)"),
            ("", "carrier", "VARCHAR(50)"),
            ("", "telecom_type", "VARCHAR(30)"),
            ("", "risk_level", "VARCHAR(20)"),
            ("", "total_reports", "INT"),
            ("", "is_blacklisted", "BOOLEAN"),
            ("", "first_reported_at", "TIMESTAMPTZ"),
            ("", "last_reported_at", "TIMESTAMPTZ"),
            ("", "created_at", "TIMESTAMPTZ"),
        ]
    },
    "malicious_domains": {
        "x": 580, "y": 940, "w": 330,
        "color": "#fff2cc", "stroke": "#d6b656",
        "cols": [
            ("PK", "id", "UUID"),
            ("", "domain", "VARCHAR(255)"),
            ("", "original_url", "TEXT"),
            ("", "threat_type", "VARCHAR(50)"),
            ("", "target_brand", "VARCHAR(100)"),
            ("", "is_active", "BOOLEAN"),
            ("", "reported_count", "INT"),
            ("", "created_at", "TIMESTAMPTZ"),
        ]
    },
    "lookup_history": {
        "x": 580, "y": 1200, "w": 330,
        "color": "#d5e8d4", "stroke": "#82b366",
        "cols": [
            ("PK", "id", "UUID"),
            ("FK", "user_id", "UUID"),
            ("", "entity_type", "VARCHAR(30)"),
            ("", "entity_value", "VARCHAR(255)"),
            ("", "risk_score", "DOUBLE PRECISION"),
            ("", "risk_level", "VARCHAR(30)"),
            ("", "penalty_breakdown", "JSONB"),
            ("", "ip_address", "VARCHAR(45)"),
            ("", "lat", "DOUBLE PRECISION"),
            ("", "lng", "DOUBLE PRECISION"),
            ("", "created_at", "TIMESTAMPTZ"),
        ]
    },

    # Column 3: Scam Reports, Attachments & Hashes (Purple)
    "incident_categories": {
        "x": 1090, "y": 60, "w": 350,
        "color": "#e1d5e7", "stroke": "#9673a6",
        "cols": [
            ("PK", "id", "UUID"),
            ("", "code", "VARCHAR(50)"),
            ("", "name", "VARCHAR(150)"),
            ("", "description", "TEXT"),
            ("", "base_penalty_score", "DOUBLE PRECISION"),
            ("", "is_active", "BOOLEAN"),
            ("", "created_at", "TIMESTAMPTZ"),
        ]
    },
    "scam_reports": {
        "x": 1090, "y": 300, "w": 350,
        "color": "#e1d5e7", "stroke": "#9673a6",
        "cols": [
            ("PK", "id", "UUID"),
            ("FK", "reporter_id", "UUID"),
            ("FK", "category_id", "UUID"),
            ("", "entity_type", "VARCHAR(30)"),
            ("", "entity_value", "VARCHAR(255)"),
            ("FK", "bank_account_id", "UUID"),
            ("FK", "phone_number_id", "UUID"),
            ("FK", "domain_id", "UUID"),
            ("", "title", "VARCHAR(250)"),
            ("", "description", "TEXT"),
            ("", "scam_amount", "NUMERIC(15,2)"),
            ("", "status", "VARCHAR(30)"),
            ("FK", "reviewer_id", "UUID"),
            ("", "reviewer_note", "TEXT"),
            ("", "reviewed_at", "TIMESTAMPTZ"),
            ("", "lat", "DOUBLE PRECISION"),
            ("", "lng", "DOUBLE PRECISION"),
            ("", "created_at", "TIMESTAMPTZ"),
        ]
    },
    "evidence_attachments": {
        "x": 1090, "y": 760, "w": 350,
        "color": "#e1d5e7", "stroke": "#9673a6",
        "cols": [
            ("PK", "id", "UUID"),
            ("FK", "report_id", "UUID"),
            ("", "file_type", "VARCHAR(50)"),
            ("", "file_url", "TEXT"),
            ("", "file_size_bytes", "BIGINT"),
            ("", "ocr_extracted_text", "TEXT"),
            ("", "created_at", "TIMESTAMPTZ"),
        ]
    },
    "image_hashes": {
        "x": 1090, "y": 990, "w": 350,
        "color": "#e1d5e7", "stroke": "#9673a6",
        "cols": [
            ("PK", "id", "UUID"),
            ("FK", "report_id", "UUID"),
            ("FK", "attachment_id", "UUID"),
            ("", "phash", "VARCHAR(64)"),
            ("", "image_url", "TEXT"),
            ("", "created_at", "TIMESTAMPTZ"),
        ]
    },

    # Column 4: Disputes, Audit & Configuration (Orange/Coral)
    "disputes": {
        "x": 1620, "y": 300, "w": 340,
        "color": "#ffe6cc", "stroke": "#d79b00",
        "cols": [
            ("PK", "id", "UUID"),
            ("FK", "report_id", "UUID"),
            ("FK", "applicant_id", "UUID"),
            ("", "applicant_name", "VARCHAR(100)"),
            ("", "applicant_phone", "VARCHAR(20)"),
            ("", "citizen_id", "VARCHAR(20)"),
            ("", "reason", "TEXT"),
            ("", "citizen_id_front_url", "TEXT"),
            ("", "citizen_id_back_url", "TEXT"),
            ("", "bank_confirmation_url", "TEXT"),
            ("", "status", "VARCHAR(30)"),
            ("FK", "reviewer_id", "UUID"),
            ("", "resolution_note", "TEXT"),
            ("", "resolved_at", "TIMESTAMPTZ"),
            ("", "created_at", "TIMESTAMPTZ"),
        ]
    },
    "audit_logs": {
        "x": 1620, "y": 720, "w": 340,
        "color": "#f8cecc", "stroke": "#b85450",
        "cols": [
            ("PK", "id", "UUID"),
            ("FK", "actor_id", "UUID"),
            ("", "action", "VARCHAR(50)"),
            ("", "target_table", "VARCHAR(50)"),
            ("", "target_id", "UUID"),
            ("", "old_values", "JSONB"),
            ("", "new_values", "JSONB"),
            ("", "ip_address", "VARCHAR(45)"),
            ("", "user_agent", "TEXT"),
            ("", "created_at", "TIMESTAMPTZ"),
        ]
    },
    "system_configs": {
        "x": 1620, "y": 1030, "w": 340,
        "color": "#ffe6cc", "stroke": "#d79b00",
        "cols": [
            ("PK", "id", "UUID"),
            ("", "config_key", "VARCHAR(100)"),
            ("", "config_value", "VARCHAR(255)"),
            ("", "value_type", "VARCHAR(20)"),
            ("", "description", "TEXT"),
            ("FK", "updated_by", "UUID"),
            ("", "updated_at", "TIMESTAMPTZ"),
        ]
    }
}

# Explicit Relationship Routing definitions (Source Table -> Target Table)
# Each has distinct waypoints so lines NEVER share coordinates or overlap!
RELATIONSHIPS = [
    # 1. users -> user_devices (Left channel X=40)
    {
        "id": "rel_users_devices", "name": "has_devices",
        "src": "users", "src_col": "id",
        "tgt": "user_devices", "tgt_col": "user_id",
        "points": [(80, 110), (45, 110), (45, 390), (80, 390)]
    },
    # 2. users -> family_guardians (user_id) (Left channel X=30)
    {
        "id": "rel_users_guardians_u", "name": "requests_protection",
        "src": "users", "src_col": "id",
        "tgt": "family_guardians", "tgt_col": "user_id",
        "points": [(80, 140), (30, 140), (30, 690), (80, 690)]
    },
    # 3. users -> family_guardians (guardian_id) (Left channel X=15)
    {
        "id": "rel_users_guardians_g", "name": "acts_as_guardian",
        "src": "users", "src_col": "id",
        "tgt": "family_guardians", "tgt_col": "guardian_id",
        "points": [(80, 170), (15, 170), (15, 715), (80, 715)]
    },
    # 4. users -> sos_alerts (user_id) (Left channel X=5)
    {
        "id": "rel_users_sos", "name": "triggers_sos",
        "src": "users", "src_col": "id",
        "tgt": "sos_alerts", "tgt_col": "user_id",
        "points": [(80, 200), (0, 200), (0, 950), (80, 950)]
    },
    # 5. sos_alerts -> sos_alert_recipients (alert_id) (Direct vertical in Col 1)
    {
        "id": "rel_sos_recipients", "name": "notifies_guardians",
        "src": "sos_alerts", "src_col": "id",
        "tgt": "sos_alert_recipients", "tgt_col": "alert_id",
        "points": [(240, 1166), (240, 1220)]
    },
    # 6. users -> sos_alert_recipients (guardian_id) (Far left X=-15)
    {
        "id": "rel_users_sos_recipient", "name": "receives_sos",
        "src": "users", "src_col": "id",
        "tgt": "sos_alert_recipients", "tgt_col": "guardian_id",
        "points": [(80, 230), (-15, 230), (-15, 1270), (80, 1270)]
    },
    # 7. banks -> bank_accounts (Direct vertical in Col 2)
    {
        "id": "rel_banks_accounts", "name": "issues_accounts",
        "src": "banks", "src_col": "id",
        "tgt": "bank_accounts", "tgt_col": "bank_id",
        "points": [(745, 284), (745, 340)]
    },
    # 8. bank_accounts -> scam_reports (Direct horizontal Col 2 -> Col 3)
    {
        "id": "rel_accounts_reports", "name": "involved_in_report",
        "src": "bank_accounts", "src_col": "id",
        "tgt": "scam_reports", "tgt_col": "bank_account_id",
        "points": [(910, 420), (1090, 420)]
    },
    # 9. phone_numbers -> scam_reports (Direct horizontal Col 2 -> Col 3)
    {
        "id": "rel_phones_reports", "name": "reported_caller",
        "src": "phone_numbers", "src_col": "id",
        "tgt": "scam_reports", "tgt_col": "phone_number_id",
        "points": [(910, 680), (1000, 680), (1000, 450), (1090, 450)]
    },
    # 10. malicious_domains -> scam_reports (Col 2 -> Col 3 channel)
    {
        "id": "rel_domains_reports", "name": "phishing_link",
        "src": "malicious_domains", "src_col": "id",
        "tgt": "scam_reports", "tgt_col": "domain_id",
        "points": [(910, 980), (1020, 980), (1020, 480), (1090, 480)]
    },
    # 11. incident_categories -> scam_reports (Direct vertical in Col 3)
    {
        "id": "rel_categories_reports", "name": "categorizes_report",
        "src": "incident_categories", "src_col": "id",
        "tgt": "scam_reports", "tgt_col": "category_id",
        "points": [(1265, 240), (1265, 300)]
    },
    # 12. scam_reports -> evidence_attachments (Direct vertical in Col 3)
    {
        "id": "rel_reports_evidence", "name": "contains_evidence",
        "src": "scam_reports", "src_col": "id",
        "tgt": "evidence_attachments", "tgt_col": "report_id",
        "points": [(1265, 700), (1265, 760)]
    },
    # 13. scam_reports -> image_hashes (Col 3 right vertical bypass channel)
    {
        "id": "rel_reports_hashes", "name": "indexes_hashes",
        "src": "scam_reports", "src_col": "id",
        "tgt": "image_hashes", "tgt_col": "report_id",
        "points": [(1440, 640), (1460, 640), (1460, 1020), (1440, 1020)]
    },
    # 14. evidence_attachments -> image_hashes (Direct vertical in Col 3)
    {
        "id": "rel_evidence_hashes", "name": "computed_from",
        "src": "evidence_attachments", "src_col": "id",
        "tgt": "image_hashes", "tgt_col": "attachment_id",
        "points": [(1265, 940), (1265, 990)]
    },
    # 15. scam_reports -> disputes (Direct horizontal Col 3 -> Col 4)
    {
        "id": "rel_reports_disputes", "name": "subject_to_dispute",
        "src": "scam_reports", "src_col": "id",
        "tgt": "disputes", "tgt_col": "report_id",
        "points": [(1440, 340), (1620, 340)]
    },
    # 16. users -> scam_reports (reporter_id) (Through top horizontal highway Y=20)
    {
        "id": "rel_users_reports_rep", "name": "submits_report",
        "src": "users", "src_col": "id",
        "tgt": "scam_reports", "tgt_col": "reporter_id",
        "points": [(400, 90), (480, 90), (480, 20), (1050, 20), (1050, 340), (1090, 340)]
    },
    # 17. users -> scam_reports (reviewer_id) (Through horizontal highway Y=35)
    {
        "id": "rel_users_reports_rev", "name": "reviews_report",
        "src": "users", "src_col": "id",
        "tgt": "scam_reports", "tgt_col": "reviewer_id",
        "points": [(400, 120), (460, 120), (460, 35), (1070, 35), (1070, 560), (1090, 560)]
    },
    # 18. users -> lookup_history (user_id) (Channel 1-2 at X=440)
    {
        "id": "rel_users_lookup", "name": "performs_lookup",
        "src": "users", "src_col": "id",
        "tgt": "lookup_history", "tgt_col": "user_id",
        "points": [(400, 150), (440, 150), (440, 1240), (580, 1240)]
    },
    # 19. users -> disputes (reviewer_id) (Top channel Y=10)
    {
        "id": "rel_users_disputes_rev", "name": "arbitrates_dispute",
        "src": "users", "src_col": "id",
        "tgt": "disputes", "tgt_col": "reviewer_id",
        "points": [(400, 180), (500, 180), (500, 10), (1580, 10), (1580, 540), (1620, 540)]
    },
    # 20. users -> audit_logs (actor_id) (Bottom channel Y=1500)
    {
        "id": "rel_users_audit", "name": "triggers_audit",
        "src": "users", "src_col": "id",
        "tgt": "audit_logs", "tgt_col": "actor_id",
        "points": [(400, 210), (420, 210), (420, 1500), (1560, 1500), (1560, 750), (1620, 750)]
    },
    # 21. users -> system_configs (updated_by) (Bottom channel Y=1520)
    {
        "id": "rel_users_configs", "name": "modifies_config",
        "src": "users", "src_col": "id",
        "tgt": "system_configs", "tgt_col": "updated_by",
        "points": [(400, 240), (410, 240), (410, 1520), (1580, 1520), (1580, 1140), (1620, 1140)]
    }
]

def generate_erd():
    xml = ['<mxGraphModel dx="2800" dy="1800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="2100" pageHeight="1600" background="#ffffff" math="0" shadow="0">']
    xml.append('  <root>')
    xml.append('    <mxCell id="0"/>')
    xml.append('    <mxCell id="1" parent="0"/>')

    # Add Tables
    for t_name, t_info in TABLES.items():
        x, y, w = t_info["x"], t_info["y"], t_info["w"]
        num_cols = len(t_info["cols"])
        h = 26 + num_cols * 22
        fill = t_info["color"]
        stroke = t_info["stroke"]

        xml.append(f'    <mxCell id="e_{t_name}" value="{t_name}" style="shape=table;startSize=26;container=1;collapsible=0;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;fillColor={fill};strokeColor={stroke};strokeWidth=1.5;fontSize=12;fontFamily=Helvetica;" vertex="1" parent="1">')
        xml.append(f'      <mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>')
        xml.append('    </mxCell>')

        for idx, (pk_fk, col_name, col_type) in enumerate(t_info["cols"]):
            row_y = 26 + idx * 22
            bottom_border = 1 if idx == 0 else 0
            b_stroke = f';strokeColor={stroke};strokeWidth=1.5;' if idx == 0 else ''
            xml.append(f'    <mxCell id="r_{t_name}_{col_name}" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom={bottom_border}{b_stroke}" vertex="1" parent="e_{t_name}">')
            xml.append(f'      <mxGeometry y="{row_y}" width="{w}" height="22" as="geometry"/>')
            xml.append('    </mxCell>')

            label = f"<u><b>{col_name}</b></u>" if pk_fk == "PK" else col_name
            font_style = 4 if pk_fk == "PK" else 0
            xml.append(f'    <mxCell id="c_{t_name}_{col_name}" value="{label}" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=8;fontStyle={font_style};overflow=hidden;whiteSpace=wrap;html=1;fontSize=11;fontFamily=Helvetica;" vertex="1" parent="r_{t_name}_{col_name}">')
            xml.append(f'      <mxGeometry width="{w}" height="22" as="geometry"><mxRectangle width="{w}" height="22" as="alternateBounds"/></mxGeometry>')
            xml.append('    </mxCell>')

    # Add Relationships with explicit waypoints
    for rel in RELATIONSHIPS:
        rid = rel["id"]
        rname = rel["name"]
        src = f"e_{rel['src']}"
        tgt = f"e_{rel['tgt']}"
        pts = rel["points"]

        xml.append(f'    <mxCell id="{rid}" value="{rname}" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=ERmandOne;startFill=0;endArrow=ERzeroToMany;endFill=0;strokeColor=#333333;strokeWidth=1.4;fontSize=11;fontStyle=2;labelBackgroundColor=#ffffff;fontColor=#000000;" edge="1" parent="1" source="{src}" target="{tgt}">')
        xml.append('      <mxGeometry relative="1" as="geometry">')
        if len(pts) > 2:
            xml.append('        <Array as="points">')
            for px, py in pts:
                xml.append(f'          <mxPoint x="{px}" y="{py}"/>')
            xml.append('        </Array>')
        xml.append('      </mxGeometry>')
        xml.append('    </mxCell>')

    xml.append('  </root>')
    xml.append('</mxGraphModel>')
    return '\n'.join(xml)


def generate_rm():
    xml = ['<mxGraphModel dx="2800" dy="1800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="2100" pageHeight="1600" background="#ffffff" math="0" shadow="0">']
    xml.append('  <root>')
    xml.append('    <mxCell id="0"/>')
    xml.append('    <mxCell id="1" parent="0"/>')

    # Add Tables with 3-column layout (PK/FK | Column | Type)
    for t_name, t_info in TABLES.items():
        x, y, w = t_info["x"], t_info["y"], t_info["w"]
        num_cols = len(t_info["cols"])
        h = 26 + num_cols * 22
        fill = t_info["color"]
        stroke = t_info["stroke"]

        xml.append(f'    <mxCell id="e_{t_name}" value="{t_name}" style="shape=table;startSize=26;container=1;collapsible=0;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;align=center;resizeLast=1;html=1;fillColor={fill};strokeColor={stroke};strokeWidth=1.5;fontSize=12;fontFamily=Helvetica;" vertex="1" parent="1">')
        xml.append(f'      <mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>')
        xml.append('    </mxCell>')

        for idx, (pk_fk, col_name, col_type) in enumerate(t_info["cols"]):
            row_y = 26 + idx * 22
            bottom_border = 1 if idx == 0 else 0
            b_stroke = f';strokeColor={stroke};strokeWidth=1.5;' if idx == 0 else ''
            xml.append(f'    <mxCell id="r_{t_name}_{col_name}" value="" style="shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;top=0;left=0;right=0;bottom={bottom_border}{b_stroke}" vertex="1" parent="e_{t_name}">')
            xml.append(f'      <mxGeometry y="{row_y}" width="{w}" height="22" as="geometry"/>')
            xml.append('    </mxCell>')

            # Cell 1: PK/FK
            key_label = f"<b>{pk_fk}</b>" if pk_fk else ""
            key_color = "#b85450" if pk_fk == "PK" else ("#6c8ebf" if pk_fk == "FK" else "none")
            xml.append(f'    <mxCell id="k_{t_name}_{col_name}" value="{key_label}" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=center;fontStyle=1;overflow=hidden;whiteSpace=wrap;html=1;fontSize=10;fontColor={key_color};fontFamily=Helvetica;" vertex="1" parent="r_{t_name}_{col_name}">')
            xml.append(f'      <mxGeometry width="35" height="22" as="geometry"><mxRectangle width="35" height="22" as="alternateBounds"/></mxGeometry>')
            xml.append('    </mxCell>')

            # Cell 2: Column Name
            name_label = f"<b>{col_name}</b>" if pk_fk == "PK" else col_name
            name_w = w - 35 - 100
            xml.append(f'    <mxCell id="c_{t_name}_{col_name}" value="{name_label}" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=left;spacingLeft=6;overflow=hidden;whiteSpace=wrap;html=1;fontSize=11;fontFamily=Helvetica;" vertex="1" parent="r_{t_name}_{col_name}">')
            xml.append(f'      <mxGeometry x="35" width="{name_w}" height="22" as="geometry"><mxRectangle width="{name_w}" height="22" as="alternateBounds"/></mxGeometry>')
            xml.append('    </mxCell>')

            # Cell 3: Data Type
            xml.append(f'    <mxCell id="t_{t_name}_{col_name}" value="{col_type}" style="shape=partialRectangle;connectable=0;fillColor=none;top=0;left=0;bottom=0;right=0;align=right;spacingRight=6;overflow=hidden;whiteSpace=wrap;html=1;fontSize=10;fontColor=#666666;fontFamily=Helvetica;" vertex="1" parent="r_{t_name}_{col_name}">')
            xml.append(f'      <mxGeometry x="{35 + name_w}" width="100" height="22" as="geometry"><mxRectangle width="100" height="22" as="alternateBounds"/></mxGeometry>')
            xml.append('    </mxCell>')

    # In Relational Model, arrow points from FK to PK!
    for rel in RELATIONSHIPS:
        rid = f"rm_{rel['id']}"
        src_table = rel["src"]
        tgt_table = rel["tgt"]
        src = f"e_{src_table}"
        tgt = f"e_{tgt_table}"
        pts = rel["points"]

        # RM arrow points from FK to PK (tgt -> src)
        # We reverse points for directional clarity
        rm_pts = list(reversed(pts))

        xml.append(f'    <mxCell id="{rid}" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;startArrow=none;endArrow=classic;endFill=1;strokeColor=#1e293b;strokeWidth=1.5;" edge="1" parent="1" source="{tgt}" target="{src}">')
        xml.append('      <mxGeometry relative="1" as="geometry">')
        if len(rm_pts) > 2:
            xml.append('        <Array as="points">')
            for px, py in rm_pts:
                xml.append(f'          <mxPoint x="{px}" y="{py}"/>')
            xml.append('        </Array>')
        xml.append('      </mxGeometry>')
        xml.append('    </mxCell>')

    xml.append('  </root>')
    xml.append('</mxGraphModel>')
    return '\n'.join(xml)

if __name__ == "__main__":
    erd_content = generate_erd()
    with open(ERD_PATH, "w", encoding="utf-8") as f:
        f.write(erd_content)
    print(f"Generated ERD: {ERD_PATH} ({len(erd_content)} chars)")

    rm_content = generate_rm()
    with open(RM_PATH, "w", encoding="utf-8") as f:
        f.write(rm_content)
    print(f"Generated RM: {RM_PATH} ({len(rm_content)} chars)")

