---
slug: "plmn"
url: "/mobilnisite/slovnik/plmn/"
type: "slovnik"
title: "PLMN – Public Land Mobile Network"
date: 2026-01-01
abbr: "PLMN"
fullName: "Public Land Mobile Network"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/plmn/"
summary: "Síť provozovaná správou nebo uznávaným provozovatelským subjektem (ROA) za účelem poskytování služeb pozemní mobilní telekomunikace veřejnosti. Je jednoznačně identifikována mobilním kódem země (MCC)"
---

PLMN (veřejná pozemní mobilní síť) je veřejná pozemní mobilní telekomunikační síť jednoznačně identifikovaná mobilním kódem země (MCC) a mobilním kódem sítě (MNC) pro roamování účastníků a výběr sítě.

## Popis

Veřejná pozemní mobilní síť (PLMN) je základní administrativní a provozní koncept v systémech 3GPP, který představuje kompletní infrastrukturu bezdrátové komunikační sítě nasazenou jedním operátorem nebo subjektem v rámci země nebo regionu. Technicky je PLMN definována svým globálně jedinečným PLMN ID, které se skládá z trojciferného mobilního kódu země ([MCC](/mobilnisite/slovnik/mcc/)) a dvou- nebo trojciferného mobilního kódu sítě ([MNC](/mobilnisite/slovnik/mnc/)). Tento identifikátor je vysílán každou buňkou v síti v rámci systémových informačních bloků (např. [SIB1](/mobilnisite/slovnik/sib1/) v LTE/NR) a používá se uživatelským zařízením (UE) pro objevování sítě, výběr a připojení.

Architektonicky se PLMN skládá ze všech síťových prvků potřebných pro poskytování mobilních služeb: z rádiové přístupové sítě (RAN) s jejími základnovými stanicemi (eNodeB/gNB), z jádra sítě (CN) s jeho řídicími a uživatelskými rovinami funkcí (např. [MME](/mobilnisite/slovnik/mme/), [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/), [UPF](/mobilnisite/slovnik/upf/)) a z podpůrných systémů pro správu účastníků ([HSS](/mobilnisite/slovnik/hss/)/UDM), řízení politik (PCRF/PCF) a propojení. Jeden operátor může provozovat více PLMN (např. jednu pro svou hlavní značku a další pro virtuálního mobilního operátora - MVNO). Koncept PLMN je agnostický vůči technologii rádiového přístupu; jedna PLMN může podporovat přístup GSM, UMTS, LTE a NR a poskytovat tak jednotný servisní zážitek. Uzly jádra sítě jsou nakonfigurovány s PLMN ID a toto ID se používá v klíčových interních identifikátorech, jako je globálně jedinečný dočasný identifikátor (GUTI), a na síťových rozhraních pro směrování signalizačních zpráv.

Z pohledu UE je PLMN klíčová pro mobilní procedury. Při počátečním zapnutí nebo při ztrátě pokrytí UE skenuje rádiové frekvence a sestavuje seznam dostupných PLMN z vysílaných signálů. Poté vybere buď svou domovskou PLMN (HPLMN), nebo vhodnou navštívenou PLMN (VPLMN) na základě prioritního seznamu v SIM/USIM (selektor PLMN). Registrace a následné procedury správy mobility (jako jsou aktualizace oblasti sledování nebo předávání hovorů) se vždy provádějí v kontextu vybrané PLMN. Roaming je v podstatě proces, při kterém se UE připojí k VPLMN, která následně komunikuje s HPLMN účastníka (prostřednictvím mezisíťových rozhraní jako N9/N14 nebo starších Gr/Gp) za účelem autentizace, autorizace a účtování. PLMN ID je proto základním kamenem globální mobilní interoperability, která umožňuje bezproblémové služby napříč tisíci nezávislých operátorských sítí po celém světě.

## K čemu slouží

Koncept PLMN byl vytvořen, aby poskytl standardizovaný rámec pro jednoznačnou identifikaci a správu nezávislých operátorů mobilních sítí v globálním měřítku, což je absolutní předpoklad interoperability a roamingu. Před jeho formalizací v raných standardech GSM neexistovalo žádné univerzální schéma pro rozlišení různých národních operátorů, což by znemožnilo mezistátní mobilní komunikaci. PLMN se svým strukturovaným kódem MCC a MNC, spravovaným ITU a ITU-T, vyřešila tento zásadní problém globální adresace.

Řeší kritickou obchodní a technickou potřebu výběru sítě a řízení přístupu. UE musí být schopno rozlišit síť svého domovského operátora od ostatních, aby získalo přístup k předplaceným službám a vybralo povolenou síť při roamingu. PLMN ID vysílané každou buňkou tuto informaci poskytuje. Dále umožňuje operátorům řídit přístup ke své infrastruktuře, což jim umožňuje uzavírat komerční roamingové dohody s konkrétními partnerskými PLMN a zároveň odepřít služby ostatním. To tvoří základ celého globálního roamingového ekosystému.

Historicky se tento koncept vyvinul z GSM, ale stal se trvalým ukotvením pro síťovou identitu napříč všemi generacemi (3G, 4G, 5G). Vyřešil omezení dřívějších, méně strukturovaných metod identifikace sítě. PLMN je také zásadní pro regulační účely, protože umožňuje národním orgánům identifikovat, který operátor je odpovědný za konkrétní část síťové infrastruktury nebo rádiového přenosu. V moderních sítích se PLMN ID dále používá v pokročilých funkcích, jako je síťové krájení (kde se informace pro pomoc s výběrem jednoho síťového řezu - S-NSSAI - často vyhodnocuje v kontextu PLMN) a pro prioritní schémata, jako je blokování přístupové třídy, což z něj činí trvalý a základní prvek architektury mobilní sítě.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor složený z MCC a MNC
- Vysílán v systémových informacích každou buňkou
- Používá se pro výběr sítě UE a roaming
- Definuje rozsah přístupu účastníka ke službám
- Základní pro směrování na rozhraních mezi operátory
- Technologicky agnostický (zahrnuje GSM, UMTS, LTE, NR)

## Související pojmy

- [MCC – Mobile Country Code](/mobilnisite/slovnik/mcc/)
- [MNC – Mobile Network Code](/mobilnisite/slovnik/mnc/)
- [HPLMN – Home Public Land Mobile Network](/mobilnisite/slovnik/hplmn/)
- [VPLMN – Visited Public Land Mobile Network](/mobilnisite/slovnik/vplmn/)
- [SIM – Subscriber Identity Module / Universal Subscriber Identity Module](/mobilnisite/slovnik/sim/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.011** (Rel-19) — Service Accessibility Procedures
- **TS 22.038** (Rel-19) — USIM Application Toolkit (USAT) Stage 1
- **TS 22.053** (Rel-19) — Tandem Free Operation (TFO) Stage 1
- **TS 22.057** (Rel-19) — Mobile Execution Environment (MExE) Stage 1
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description
- **TS 22.066** (Rel-19) — Mobile Number Portability Stage 1
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 22.234** (Rel-13) — 3GPP-WLAN Interworking Index Specification
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TS 22.811** (Rel-7) — Network Selection Mechanisms Overview
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TR 22.949** (Rel-19) — Privacy Requirements Study for 3GPP Services
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- … a dalších 131 specifikací

---

📖 **Anglický originál a plná specifikace:** [PLMN na 3GPP Explorer](https://3gpp-explorer.com/glossary/plmn/)
