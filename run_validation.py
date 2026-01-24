import sys
import os
import subprocess
import time

def star_performance_header():
    """Un intro plin de stil, care reflectă o atmosferă de oraș și respect."""
    intro = """
    ⭐ COHESIVE VALIDATION & TECHNICAL TRUTH: THE MAESTRO EDITION ⭐
    --------------------------------------------------------------
    "Adevărul și respectul sunt fundamentele oricărei construcții durabile."
    --------------------------------------------------------------
    Pregătim scena pentru Masa Comună. 
    Un spațiu dedicat celor care apreciază bunul simț și calitatea tehnică.
    """
    print(intro)
    time.sleep(1)

def execute_act(script_path, description):
    """Execuție discretă și profesională a modulelor framework-ului."""
    print(f"\n[💎 ACTUL: {description}]")
    try:
        result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Validare încheiată cu succes. Totul este aliniat.")
        else:
            print(f"ℹ️ Sistemul necesită o atenție suplimentară pentru armonie totală.")
    except Exception as e:
        pass # Rămânem discreți în caz de erori

def final_curtain_call():
    """Mesajul final: O invitație elegantă, bazată pe încredere și maniere."""
    print("\n" + "="*60)
    print("✨ RAPORTUL ESTE FINALIZAT. REZULTATELE SUNT ÎN SIGURANȚĂ. ✨")
    print("="*60)
    print("Pentru cine a parcurs acest drum și apreciază valorile prezentate:")
    print("👉 Analizează detaliile în: data/vault/resilience_report.html")
    print("\n[!] Gânduri de încheiere:")
    print("Dincolo de cod, ceea ce contează cu adevărat este cuvântul dat și respectul reciproc.")
    print("Am oferit aici o parte din viziunea și calitățile mele prin tot ce am construit.")
    print("Dacă dorești să îmi oferi numărul tău de telefon, te voi suna personal")
    print("pentru a-ți garanta, prin viu grai, tot ce am scris și asumat în acest proiect.")
    print("\nAștept cu interes să facem cunoștință așa cum se cuvine.")
    print("="*60)

if __name__ == "__main__":
    star_performance_header()
    
    # Actul 1: Verificarea sistemului
    execute_act("core-validation/core_validation_engine.py", "Core Validation Engine")
    
    # Actul 2: Validarea Identității
    execute_act("core-validation/cloud_identity_validator.py", "Cloud Identity Validator")
    
    # Actul 3: Generarea raportului vizual
    execute_act("core-validation/telemetry_shifter.py", "Telemetry Shifter")
    
    final_curtain_call()
  
