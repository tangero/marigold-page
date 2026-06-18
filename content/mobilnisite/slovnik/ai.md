---
slug: "ai"
url: "/mobilnisite/slovnik/ai/"
type: "slovnik"
title: "AI – Application Interface"
date: 2026-01-01
abbr: "AI"
fullName: "Application Interface"
category: "Interface"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ai/"
summary: "AI je předpona používaná ve specifikacích 3GPP pro označení aplikačního rozhraní (Application Interface), konkrétně třídní metody v rámci rozhraní. Standardizuje pojmenování rozhraní na aplikační úrov"
---

AI je předpona používaná ve specifikacích 3GPP pro označení aplikačního rozhraní (Application Interface), konkrétně třídní metody, která standardizuje pojmenování rozhraní na aplikační úrovni pro síťové funkce a služby.

## Popis

Ve specifikacích 3GPP slouží termín 'AI' jako standardizovaná předpona pro třídní metody aplikačního rozhraní (Application Interface). Jedná se o konvenci pojmenování používanou v rámci definic rozhraní pro jednoznačnou identifikaci metod, které patří do aplikační vrstvy síťových funkcí. Tato předpona se používá napříč různými technickými specifikacemi (TS), aby byla zachována konzistence v dokumentaci a implementaci aplikačních programových rozhraní ([API](/mobilnisite/slovnik/api/)) a rozhraní založených na službách ([SBI](/mobilnisite/slovnik/sbi/)).

Předpona AI se typicky vyskytuje v kontextu architektury otevřených služeb ([OSA](/mobilnisite/slovnik/osa/)) a později v architektuře založené na službách ([SBA](/mobilnisite/slovnik/sba/)) jádra sítě 5G. Předchází vlastní název metody a vytváří tak úplný identifikátor, například 'AI_<NázevMetody>'. Toto strukturované pojmenování pomáhá odlišit operace aplikační vrstvy od funkcí transportní, relační nebo managementové vrstvy v rámci složitých rozhraní síťových prvků. Samotné metody definují operace, které může aplikace vyvolat na síťové funkci, nebo které si síťové funkce mohou vzájemně zpřístupňovat, jako je registrace služeb, jejich vyhledávání, vyvolání a správa politik.

Z architektonického hlediska jsou rozhraní používající předponu AI součástí širšího rámce pro umožnění interakce aplikací třetích stran se síťovými schopnostmi, jak je definováno ve specifikacích jako TS 23.090 (Open Service Access) a TS 23.271 (Location Services). V moderních systémech 5G se tento koncept vyvíjí ve směru funkce pro vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)) a standardizovaných API, ale předpona AI historicky poskytovala jasný marker pro metody relevantní pro aplikace v rámci specifikací rozhraní. Její použití zajišťuje, že při návrhu systému, generování kódu a testování mohou inženýři snadno identifikovat a zpracovat metody určené pro aplikační logiku a vystavení služeb.

## K čemu slouží

Předpona AI byla zavedena, aby vyřešila problém nekonzistentního a nejednoznačného pojmenování metod aplikační vrstvy v rámci specifikací rozhraní 3GPP. Před její standardizací mohly různé pracovní skupiny a vydání používat pro podobné metody rozhraní rozdílné konvence pojmenování (jako 'App', 'Srv' nebo žádnou předponu), což vedlo ke zmatkům při implementaci a integraci mezi síťovými zařízeními od různých dodavatelů. Předpona vytváří jednotný, snadno rozpoznatelný vzor, který označuje, že metoda patří do domény aplikačního rozhraní.

Její zavedení bylo motivováno potřebou jasných, udržovatelných a interoperabilních specifikací v době, kdy sítě 3GPP začaly vystavovat více schopností externím aplikacím, počínaje iniciativami jako Open Service Access ([OSA](/mobilnisite/slovnik/osa/)) a Parlay/OSA [API](/mobilnisite/slovnik/api/). Označením těchto metod předponou 'AI' zajistil standardizační orgán, že kdokoli čte technickou specifikaci, může okamžitě pochopit funkční vrstvu operace, čímž se zjednodušil vývoj síťových prvků a klientských aplikací, které na těchto standardizovaných rozhraních závisí.

## Klíčové vlastnosti

- Standardizovaná předpona pro třídní metody aplikačního rozhraní
- Zvyšuje přehlednost a čitelnost specifikací
- Usnadňuje konzistentní implementaci napříč dodavateli
- Označuje metody patřící do aplikační vrstvy síťových funkcí
- Používá se jak v architekturách OSA/Parlay, tak v architekturách založených na službách
- Podporuje automatické generování kódu ze specifikací

## Související pojmy

- [OSA – Open Services Architecture](/mobilnisite/slovnik/osa/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [API – Application Programming Interface](/mobilnisite/slovnik/api/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.156** (Rel-19) — Mobile Metaverse Services
- **TR 22.829** (Rel-17) — Enhancement for UAVs; Stage 1
- **TR 22.856** (Rel-19) — Feasibility Study on Localized Mobile Metaverse Services
- **TR 22.873** (Rel-18) — Technical Report on IMS Multimedia Telephony Service Enhancements
- **TR 22.874** (Rel-18) — Technical Report
- **TR 22.890** (Rel-19) — Study on Railway Smart Station Services
- **TS 23.090** (Rel-19) — USSD Stage 2 Specification
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 26.847** (Rel-19) — AI/ML Evaluation in 5G Media Services
- **TS 26.854** (Rel-19) — Study on Haptics in 5G Media Services
- **TR 26.927** (Rel-19) — AI/ML in 5G Media Services Study
- … a dalších 15 specifikací

---

📖 **Anglický originál a plná specifikace:** [AI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ai/)
