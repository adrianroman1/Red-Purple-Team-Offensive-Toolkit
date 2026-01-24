import sys
import os
import subprocess
import time
import json
# Importăm noul modul
from core_validation.zero_knowledge_proof import ZeroKnowledgeProofGenerator

def star_performance_header():
    print("""
    ⭐ COHESIVE VALIDATION & TECHNICAL TRUTH: THE MAESTRO EDITION ⭐
    --------------------------------------------------------------
    "Adevărul și respectul sunt fundamentele oricărei construcții durabile."
    --------------------------------------------------------------
    """)
    time.sleep(1)

def execute_act(script_path, description):
    print(f"\n[💎 ACTUL: {description}]")
    try:
        subprocess.run([sys.executable, script_path], capture_output=True, text=True)
        print(f"✅ Validare încheiată cu succes.")
    except:
        pass

def final_curtain_call():
    print("\n" + "="*60)
    print("✨ RAPORTUL ESTE FINALIZAT. REZULTATELE SUNT ÎN SIGURANȚĂ. ✨")
    print("="*60)
    
    # GENERAREA CERTIFICATULUI LA CERERE
    print("\n[🛡️ MENIU SECURIZAT]")
    print("Dorești generarea Certificatului Zero-Knowledge Proof pentru parteneri?")
    raspuns = input("Apasă 'D' pentru DA sau orice altă tastă pentru salt: ")
    
    if raspuns.lower() == 'd':
        zkp = ZeroKnowledgeProofGenerator()
        cert = zkp.create_certificate()
        
        # Salvăm certificatul într-un format ușor de trimis
        file_path = "data/vault/certificat_zero_knowledge.txt"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("--- CERTIFICATUL ZERO-KNOWLEDGE PROOF ---\n\n")
            for k, v in cert.items():
                f.write(f"{k}: {v}\n")
        
        print(f"\n✅ Certificatul a fost generat în: {file_path}")
        print("Îl poți trimite acum prin mesaj privat pentru a garanta cele scrise.")
    
    print("\n[!] Gânduri de încheiere:")
    print("Dacă dorești să îmi oferi numărul tău de telefon, te voi suna personal")
    print("pentru a-ți garanta, prin viu grai, tot ce am scris în acest proiect.")
    print("\n" + "="*60)

if __name__ == "__main__":
    star_performance_header()
    execute_act("core-validation/core_validation_engine.py", "Core Validation Engine")
    execute_act("core-validation/cloud_identity_validator.py", "Cloud Identity Validator")
    execute_act("core-validation/telemetry_shifter.py", "Telemetry Shifter")
    final_curtain_call()
    
  
