---
slug: "gmk-id"
url: "/mobilnisite/slovnik/gmk-id/"
type: "slovnik"
title: "GMK-ID – Group Master Key Identifier"
date: 2026-01-01
abbr: "GMK-ID"
fullName: "Group Master Key Identifier"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gmk-id/"
summary: "Identifikátor používaný v sítích 3GPP k jednoznačné referenci na skupinový hlavní klíč (GMK) v rámci bezpečnostních kontextů skupinové komunikace. Umožňuje bezpečnou správu skupin pro služby jako ProS"
---

GMK-ID je identifikátor používaný v sítích 3GPP k jednoznačné referenci na skupinový hlavní klíč (Group Master Key) v rámci bezpečnostních kontextů skupinové komunikace pro služby jako ProSe, V2X a MBMS.

## Popis

Identifikátor skupinového hlavního klíče (GMK-ID) je kritický bezpečnostní parametr v architektuře skupinové komunikace 3GPP, definovaný primárně pro služby jako Proximity Services ([ProSe](/mobilnisite/slovnik/prose/)), komunikace Vehicle-to-Everything ([V2X](/mobilnisite/slovnik/v2x/)) a Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)). Funguje jako jedinečná značka nebo reference, která odkazuje na konkrétní skupinový hlavní klíč ([GMK](/mobilnisite/slovnik/gmk/)), což je kořenový kryptografický klíč používaný k odvození podřízených klíčů pro zabezpečení skupinové komunikace. Samotný GMK je symetrický klíč, typicky distribuovaný centrem správy klíčů nebo skupinovým kontrolérem, a používá se k vytváření šifrovacích klíčů pro provoz ([TEK](/mobilnisite/slovnik/tek/)) a dalšího klíčového materiálu pro šifrování a ochranu integrity dat odesílaných skupině uživatelů. GMK-ID neobsahuje samotný klíčový materiál, ale slouží jako index, který umožňuje autorizovaným síťovým funkcím a uživatelským zařízením (UE) vyžádat nebo identifikovat správný GMK ze serveru správy klíčů nebo lokálního úložiště na základě skupinového kontextu.

Z architektonického hlediska se GMK-ID používá v bezpečnostních protokolech a rozhraních definovaných pro skupinovou komunikaci. Například v ProSe a V2X je GMK-ID referencován v signalizačních zprávách mezi funkcí ProSe, funkcí správy klíčů (KMF) a uživatelským zařízením (UE). Když se UE připojí ke skupině nebo potřebuje v rámci skupiny komunikovat bezpečně, může jako součást autorizace členství ve skupině obdržet GMK-ID. UE poté použije tento GMK-ID k získání odpovídajícího GMK z bezpečného úložiště klíčů nebo k odvození relakčních klíčů. Toto oddělení identifikátoru a klíče zvyšuje bezpečnost tím, že omezuje vystavení skutečného klíče během přenosu a zjednodušuje správu životního cyklu klíčů – klíče lze aktualizovat nebo rotovat při zachování konstantního GMK-ID pro kontinuitu.

Role GMK-ID se rozšiřuje o zajištění škálovatelnosti a efektivity ve správě skupinových klíčů. Ve velkých nasazeních, jako je MBMS, kde mohou tisíce uživatelů odebírat vysílací službu, GMK-ID pomáhá zefektivnit distribuci klíčů. Síť může vysílat GMK-ID spolu se šifrovaným obsahem a pouze autorizovaná UE s odpovídajícím GMK jej mohou dešifrovat. To snižuje signalizační režii ve srovnání s distribucí klíčů na jednoho uživatele. Specifikace jako 3GPP TS 33.179 a TS 33.180 detailně popisují použití GMK-ID v zabezpečení V2X, zatímco TS 24.380 a TS 29.380 pokrývají jeho aplikaci v ProSe. Identifikátor je typicky formátován jako binární nebo alfanumerický řetězec, jehož struktura a kódování jsou specifikovány v příslušných protokolech, aby byla zajištěna interoperabilita mezi různými síťovými prvky a releasy.

## K čemu slouží

GMK-ID byl zaveden, aby řešil rostoucí potřebu bezpečné skupinové komunikace v sítích 3GPP, zejména s nástupem služeb jako [ProSe](/mobilnisite/slovnik/prose/) a [V2X](/mobilnisite/slovnik/v2x/) ve Release 13 a novějších. Před jeho zavedením skupinová komunikace často spoléhala na párové bezpečnostní klíče nebo méně škálovatelné metody, které byly neefektivní pro dynamické skupiny, kde členové často přistupují nebo odcházejí. GMK-ID umožňuje efektivní správu klíčů tím, že odděluje identifikátor klíče od klíčového materiálu, což umožňuje bezpečné získávání a aktualizace klíčů bez nutnosti znovu navazovat skupinové kontexty.

Historicky, jak se 3GPP vyvíjelo pro podporu IoT, veřejné bezpečnosti a automobilových aplikací, se projevila omezení stávajících bezpečnostních mechanismů. Například v raných implementacích [MBMS](/mobilnisite/slovnik/mbms/) byla distribuce klíčů více centralizovaná a méně flexibilní, což ztěžovalo podporu formování skupin v reálném čase ve scénářích V2X. GMK-ID jako součást širšího rámce skupinové bezpečnosti to řeší tím, že poskytuje odlehčenou referenci, která usnadňuje dynamické odvozování a distribuci klíčů. Podporuje scénáře, kdy jsou skupiny dočasné nebo geograficky rozptýlené, jako je formování kolon vozidel nebo komunikace pro veřejnou bezpečnost, a zajišťuje, že pouze autorizovaní členové mají přístup ke skupinovým datům.

GMK-ID dále zvyšuje bezpečnost snížením rizika vystavení klíče během přenosu. Protože je přenášen pouze identifikátor po rádiovém rozhraní nebo síťových rozhraních, zůstává skutečný GMK chráněn v bezpečném úložišti. To je v souladu s bezpečnostními principy 3GPP týkajícími se důvěrnosti a integrity a řeší hrozby jako odposlech nebo replay útoky ve skupinovém prostředí. Jeho vytvoření bylo motivováno potřebou standardizovaného, interoperabilního přístupu ke správě skupinových klíčů napříč více releasy a službami, což umožňuje plynulý vývoj od LTE k 5G a dále.

## Klíčové vlastnosti

- Jednoznačně identifikuje skupinový hlavní klíč (GMK) pro zabezpečenou skupinovou komunikaci
- Umožňuje efektivní získávání a správu klíčů v dynamických skupinových scénářích
- Podporuje služby jako ProSe, V2X a MBMS pro škálovatelné zabezpečení
- Odděluje referenci na klíč od klíčového materiálu pro zvýšení bezpečnosti přenosu
- Usnadňuje rotaci a aktualizaci klíčů bez narušení členství ve skupině
- Interoperabilní napříč více releasy 3GPP a síťovými architekturami

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 24.582** (Rel-19) — MCData Media Plane Control Protocols
- **TS 29.380** (Rel-19) — MCPTT-LMR Interworking Media Plane Control
- **TS 29.582** (Rel-19) — MCData Interworking with LMR Systems
- **TS 33.179** (Rel-13) — MCPTT Security Architecture and Procedures
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.879** (Rel-13) — MCPTT Security Study

---

📖 **Anglický originál a plná specifikace:** [GMK-ID na 3GPP Explorer](https://3gpp-explorer.com/glossary/gmk-id/)
