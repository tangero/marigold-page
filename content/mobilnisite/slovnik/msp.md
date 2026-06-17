---
slug: "msp"
url: "/mobilnisite/slovnik/msp/"
type: "slovnik"
title: "MSP – Mobile Subscriber Provisioning"
date: 2025-01-01
abbr: "MSP"
fullName: "Mobile Subscriber Provisioning"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/msp/"
summary: "MSP označuje entitu účastníka zřízenou konkrétními mobilními službami. Představuje účet koncového uživatele v síti a umožňuje doručování služeb a personalizaci. Tento koncept je zásadní pro správu slu"
---

MSP je entita účastníka zřízená konkrétními mobilními službami, která představuje účet koncového uživatele v síti za účelem umožnění doručování služeb a jejich personalizace.

## Popis

Mobile Subscriber Provisioning (MSP, zřízení mobilního účastníka) je klíčový koncept ve specifikacích 3GPP, který definuje účastníka jako logickou entitu zřízenou sadou služeb. MSP není fyzické zařízení (Mobile Station), ale identita předplatného (např. vázaná k [IMSI](/mobilnisite/slovnik/imsi/) nebo [MSISDN](/mobilnisite/slovnik/msisdn/)), která obsahuje profil služeb. Tento profil zahrnuje údaje jako přihlášené parametry QoS, povolené služby (např. hlas, SMS, data), oprávnění k roamingu a informace pro účtování. Entita MSP je uložena v síťových databázích, především v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) v UMTS/LTE nebo v Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) v 5GC. Když se účastník pokusí připojit k síti, síť načte profil služeb MSP, aby autorizovala relaci, použila příslušné politiky a zajistila správné účtování. MSP slouží jako kotva pro personalizaci uživatelského zážitku napříč různými přístupovými technologiemi (např. [GERAN](/mobilnisite/slovnik/geran/), UTRAN, [E-UTRAN](/mobilnisite/slovnik/e-utran/), NG-RAN) podporovanými jádrem sítě. Jeho správa zahrnuje zřizovací systémy, které naplňují HSS/UDM daty účastníka, a rozhraní s funkcemi řízení politik (jako PCRF/[PCF](/mobilnisite/slovnik/pcf/)) pro dynamickou autorizaci služeb. Koncept zajišťuje konzistentní identitu služby nezávislou na uživatelově zařízení nebo dočasné poloze.

## K čemu slouží

Koncept MSP byl formalizován, aby oddělil identitu předplatného od fyzického zařízení, což umožňuje flexibilní poskytování služeb a scénáře s více zařízeními. Před jeho jasnou definicí byly služby často pevně svázány s konkrétní SIM kartou nebo zařízením, což omezovalo personalizaci a komplikovalo přenositelnost služeb. Definováním účastníka jako zřízené entity (MSP) umožnilo 3GPP operátorům nabízet komplexní balíčky služeb, roamingové dohody a konvergentní účtování napříč okruhově a paketově spínanými doménami. Vyřešilo problém správy uživatelsky orientovaných služeb standardizovaným způsobem a poskytlo jasný referenční bod pro autorizaci služeb, správu mobility a účtovací funkce. Vytvoření MSP bylo motivováno potřebou škálovatelné, na účastníka zaměřené architektury, která by mohla podporovat rostoucí rozmanitost mobilních služeb zaváděných od 3G (Rel-4) dále, včetně multimediálních zpráv, služeb založených na poloze a nabídek založených na IMS.

## Klíčové vlastnosti

- Představuje identitu účastníka nezávislou na uživatelském zařízení (UE).
- Ukládá profil služeb včetně přihlášených parametrů QoS a povolených služeb.
- Centralizován v HSS (3G/4G) nebo UDM (5G) pro správu nezávislou na přístupové technologii.
- Umožňuje autorizaci služeb a vynucování politik během připojování k síti.
- Tvoří základ pro přesné záznamy o účtování a fakturaci.
- Podporuje roaming prostřednictvím interakce s prvky navštívené sítě.

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.097** (Rel-19) — Multiple Subscriber Profile (MSP) service
- **TR 22.826** (Rel-17) — Study on 5G for Critical Medical Applications
- **TS 23.097** (Rel-19) — Multiple Subscriber Profile (MSP) Phase 2
- **TS 26.881** (Rel-15) — MBMS FEC for Mission Critical Services Study
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.868** (Rel-12) — Study on Group Communication for E-UTRA

---

📖 **Anglický originál a plná specifikace:** [MSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/msp/)
