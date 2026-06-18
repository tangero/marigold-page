---
slug: "nssi"
url: "/mobilnisite/slovnik/nssi/"
type: "slovnik"
title: "NSSI – Network Slice Subnet Instance"
date: 2026-01-01
abbr: "NSSI"
fullName: "Network Slice Subnet Instance"
category: "Network Slicing"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nssi/"
summary: "NSSI je spravovaná instance podmnožiny prostředků (např. skupiny síťových funkcí), která tvoří část kompletní instance end-to-end síťového řezu (NSI). Představuje nasaditelný, spravovatelný segment sí"
---

NSSI je spravovaná instance podmnožiny síťových prostředků, která tvoří modulární a nezávisle spravovatelný segment instance end-to-end síťového řezu.

## Popis

Instance podsítě síťového řezu (NSSI) je základním konceptem v architektuře síťového řezování 3GPP a představuje instanciovaný, spravovaný a provozní segment síťového řezu. Zatímco instance síťového řezu ([NSI](/mobilnisite/slovnik/nsi/)) poskytuje kompletní, end-to-end logickou síť pro konkrétní obchodní případ, NSSI tvoří funkční podmnožinu tohoto celku. NSSI je kompozicí spravovaných fyzických a/nebo virtuálních prostředků, včetně síťových funkcí ([NF](/mobilnisite/slovnik/nf/)) a potřebné konektivity mezi nimi, která poskytuje dobře definovanou sadu schopností. Více NSSI může být zkombinováno a propojeno, aby vytvořilo kompletní NSI. Například NSI pro službu tovární automatizace může být složeno ze samostatných NSSI pro část rádiového přístupového sítě (RAN), část přenosové sítě a část core sítě, každé se specifickými výkonnostními charakteristikami.

Management a orchestraci NSSI zajišťuje systém managementu a orchestrace ([MANO](/mobilnisite/slovnik/mano/)), jak je definováno ve frameworkech jako [ETSI](/mobilnisite/slovnik/etsi/) [NFV](/mobilnisite/slovnik/nfv/). Systém managementu 3GPP (3GPP [MS](/mobilnisite/slovnik/ms/)) interaguje se systémem MANO, aby vyžádal vytvoření, modifikaci, ukončení a monitoring NSSI. Každé NSSI má svůj vlastní životní cyklus, který je spravován nezávisle, ale koordinovaně pro podporu životního cyklu nadřazeného NSI. NSSI je popsáno deskriptorem podsítě síťového řezu (NSSD), což je šablona definující požadavky a charakteristiky (např. kapacita, latence, geografická oblast) podsítě. Orchestrátor používá NSSD k instanciování odpovídajícího NSSI s příslušnými prostředky.

Z provozní perspektivy NSSI umožňují modularitu, opětovné použití a efektivní využití prostředků v řezané síti. Jedna vysoce výkonná přenosová NSSI může být sdílena jako společná podsíť napříč více různými NSI (např. pro eMBB a pro [URLLC](/mobilnisite/slovnik/urllc/)), pokud jsou splněny požadavky na izolaci a výkonnostní záruky. Toto sdílení je řízeno konceptem vnořeného řezování. Schopnost nezávisle spravovat podsítě umožňuje operátorům škálovat, upgradovat nebo opravovat části síťového řezu bez nutnosti ovlivnit celou end-to-end službu. Specifikace jako TS 28.530 a TS 28.541 detailně popisují managementní procedury a rozhraní pro NSSI.

## K čemu slouží

Koncept NSSI byl vyvinut, aby řešil praktickou komplexitu nasazování a správy end-to-end síťových řezů. Vytváření monolitického [NSI](/mobilnisite/slovnik/nsi/) od nuly pro každou novou službu by bylo vysoce neefektivní a nepružné. NSSI zavádí klíčovou vrstvu dekompozice, která operátorům umožňuje stavět komplexní NSI z menších, znovupoužitelných a nezávisle spravovatelných stavebních bloků.

Tento přístup řeší několik klíčových problémů. Za prvé umožňuje sdílení a optimalizaci prostředků napříč různými řezy. Namísto vyčleňování izolovaných prostředků pro každou funkci v každém řezu mohou být společné podsítě (jako sdílená transportní vrstva) vytvořeny jednou a použity mnoha řezy, čímž se zlepšuje efektivita infrastruktury. Za druhé zjednodušuje správu životního cyklu. Upgrade síťové funkce core napříč desítkami řezů může být proveden aktualizací jedné, sdílené Core NSSI, namísto individuální modifikace každého NSI. Za třetí umožňuje, aby různými doménami (RAN, Transport, Core) spravovaly různé organizační jednotky nebo dokonce různí dodavatelé, s jasnými rozhraními definovanými hranicemi NSSI. Koncept NSSI je tedy tím, co činí rozsáhlé, komerční síťové řezování provozně proveditelným a ekonomicky životaschopným.

## Klíčové vlastnosti

- Představuje instanciovanou, spravovanou podmnožinu instance end-to-end síťového řezu (NSI)
- Definováno šablonou deskriptoru podsítě síťového řezu (NSSD)
- Nezávisle spravovaný životní cyklus (vytvoření, škálování, ukončení) prostřednictvím systémů MANO
- Může být sdíleno napříč více NSI jako společná podsíť prostředků
- Skládá se z fyzických/virtuálních síťových funkcí a jejich vzájemných propojení
- Umožňuje modulární konstrukci komplexních řezů z znovupoužitelných komponent

## Definující specifikace

- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 26.941** (Rel-19) — 5G Media Slicing Extensions
- **TS 28.530** (Rel-19) — Network Slicing Concepts & Requirements
- **TS 28.531** (Rel-20) — Management and Orchestration
- **TS 28.535** (Rel-19) — Closed Control Loop Assurance Management
- **TS 28.536** (Rel-19) — Management services for communication service assurance
- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TS 28.545** (Rel-17) — Fault Supervision for 5G Networks
- **TS 28.801** (Rel-15) — Management and Orchestration of Network Slicing
- **TR 28.808** (Rel-17) — 5G satellite integration management study
- **TR 28.841** (Rel-18) — Technical Report on IoT NTN Enhancements
- **TS 28.861** (Rel-16) — SON for 5G Networks Management
- **TS 33.811** (Rel-15) — Security study for 5G network slicing management

---

📖 **Anglický originál a plná specifikace:** [NSSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/nssi/)
