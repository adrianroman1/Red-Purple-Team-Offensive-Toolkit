import json
import os
from datetime import datetime

class TelemetryShifter:
    """Transformă datele tehnice brute într-un format vizual pentru Masa Comună."""

    def __init__(self):
        self.input_file = "data/vault/identity_truth_vault.json"
        self.output_report = "data/vault/resilience_report.html"

    def transform_to_html(self):
        """Traduce JSON-ul într-un raport vizual profesionist."""
        if not os.path.exists(self.input_file):
            return "[-] Nu s-au găsit date în vault pentru procesare."

        # Citim ultimul adevăr tehnic înregistrat
        with open(self.input_file, "r") as f:
            lines = f.readlines()
            # Luăm ultima intrare (cea mai recentă)
            data = json.loads(lines[-1])

        # Construim un HTML simplu, dar de impact (Enterprise Style)
        html_content = f"""
        <html>
        <head>
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f4f7f6; color: #333; padding: 40px; }}
                .container {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); max-width: 800px; margin: auto; }}
                h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
                .fact-box {{ background: #ecf0f1; border-left: 5px solid #3498db; padding: 15px; margin: 20px 0; }}
                .status-high {{ color: #27ae60; font-weight: bold; }}
                .footer {{ font-size: 0.8em; color: #7f8c8d; margin-top: 30px; text-align: center; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Raport de Coeziune & Reziliență Cloud</h1>
                <p><strong>Generat la:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                
                <div class="fact-box">
                    <h3>🔍 Validare Identitate</h3>
                    <p><strong>Tip Context:</strong> {data['technical_facts']['identity_context']}</p>
                    <p><strong>Nivel Permisiuni:</strong> {data['technical_facts']['role_assignment']}</p>
                    <p><strong>Integritate Token:</strong> <span class="status-high">{data['technical_facts']['token_integrity']}</span></p>
                </div>

                <div class="fact-box" style="border-left-color: #f39c12;">
                    <h3>💡 Observație pentru Masa Comună</h3>
                    <p>{data['partnership_notes']}</p>
                </div>

                <div class="footer">
                    Document generat prin Framework-ul Cohesive Cloud Validation. <br>
                    Confidențialitate: Ridicată - Destinat exclusiv discuțiilor de parteneriat.
                </div>
            </div>
        </body>
        </html>
        """

        with open(self.output_report, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        return f"[+] Raport vizual generat cu succes: {self.output_report}"

if __name__ == "__main__":
    shifter = TelemetryShifter()
    print(shifter.transform_to_html())
  
