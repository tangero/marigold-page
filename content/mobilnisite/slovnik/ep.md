---
slug: "ep"
url: "/mobilnisite/slovnik/ep/"
type: "slovnik"
title: "EP – Elementary Procedure"
date: 2025-01-01
abbr: "EP"
fullName: "Elementary Procedure"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ep/"
summary: "Základní, nedělitelná jednotka komunikace mezi síťovými entitami v systémech 3GPP. Definuje kompletní interakci, například požadavek a jeho odpověď, a je základním stavebním prvkem všech signalizačníc"
---

EP je základní, nedělitelná jednotka komunikace mezi síťovými entitami v systémech 3GPP, která definuje kompletní interakci (například požadavek a odpověď) jako základní stavební prvek všech signalizačních protokolů.

## Popis

Elementární procedura (EP) je atomickou jednotkou signalizace v protokolových specifikacích 3GPP. Představuje samostatnou transakci mezi partnerskými entitami, například mezi uživatelským zařízením (UE) a základnovou stanicí (např. gNB, [eNB](/mobilnisite/slovnik/enb/)) nebo mezi různými síťovými uzly (např. [AMF](/mobilnisite/slovnik/amf/) a [SMF](/mobilnisite/slovnik/smf/)). Každá EP je definována konkrétním účelem, jako je navázání spojení, ověření uživatele nebo předání relace. Skládá se z jedné nebo více zpráv vyměněných v definovaném pořadí, které vyústí v jednoznačný výsledek úspěchu nebo selhání. Její struktura je formalizována v dokumentech protokolových specifikací pomocí Abstract Syntax Notation One (ASN.1) nebo podobných technik formálního popisu, které detailně specifikují informační prvky zpráv, kódovací pravidla a procedurální chování jak na iniciující, tak na odpovídající straně.

Průběh EP se řídí přísným stavovým automatem. Iniciující entita odešle požadavek, čímž proceduru spustí. Příjemce tuto zprávu zpracuje, provede potřebné akce (které mohou zahrnovat interakci s jinými síťovými funkcemi nebo databázemi) a poté vrátí odpověď – buď kladnou (např. 'Požadavek přijat'), nebo zápornou (např. 'Požadavek zamítnut' s konkrétním kódem příčiny). Některé EP jsou procedury 'třídy 1', které vyžadují explicitní odpověď, zatímco jiné jsou procedury 'třídy 2', což jsou jednosměrná oznámení bez odpovědi. Úspěch EP často závisí na ověření zahrnutých parametrů a aktuálním stavu zúčastněných entit, což zajišťuje konzistentní a předvídatelný provoz sítě.

EP jsou základními stavebními kameny, z nichž jsou konstruovány složitější síťové služby a operace. Například kompletní procedura připojení (attach) UE k síti se skládá z posloupnosti více EP, včetně žádosti/odpovědi o identitu, ověření a příkazu k nastavení zabezpečení. Jsou definovány napříč všemi rozhraními specifikovanými 3GPP (např. N1, [N2](/mobilnisite/slovnik/n2/), X2, Xn, S1, Iu) a jsou nedílnou součástí protokolů, jako je Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), [NG](/mobilnisite/slovnik/ng/) Application Protocol ([NGAP](/mobilnisite/slovnik/ngap/)) a X2 Application Protocol (X2AP). Tento modulární přístup umožňuje přesnou specifikaci, testování a implementaci síťového chování, což je klíčové pro interoperabilitu zařízení od různých výrobců a pro stabilní vývoj systému napříč jednotlivými releasy.

## K čemu slouží

Elementární procedura byla vytvořena, aby poskytla standardizovanou, modulární a jednoznačnou metodu pro definování signalizačních interakcí v telekomunikačních sítích. Před takovou formalizací mohlo být chování protokolů definováno volněji, což vedlo k problémům s interoperabilitou mezi síťovým zařízením od různých výrobců. Rozdělením složitých síťových operací na atomické, přesně definované procedury 3GPP zajišťuje, že každá možná interakce má stanovený tok zpráv, ošetření chyb a výsledek, což je nezbytné pro spolehlivost a předvídatelnost rozsáhlých mobilních sítí s více dodavateli.

Její existence řeší základní problém, jak přesně navrhnout komunikaci mezi distribuovanými síťovými funkcemi. Poskytuje 'slovní zásobu' a 'gramatiku' pro spolupráci síťových entit. Například bez standardizované EP pro 'Přípravu předání hovoru' by základnová stanice jednoho výrobce mohla odesílat odlišné informace nebo očekávat jinou odpověď než stanice jiného výrobce, což by způsobovalo přerušení hovorů. EP tyto výměny formalizují a detailně specifikují každý parametr a podmínku. Tato přesnost je základem, na kterém jsou spolehlivě implementovány funkce jako správa mobility, správa relací nebo kvalita služeb.

Historicky je tento koncept ústřední pro systémy 3GPP již od GSM, ale plně byl vykrystalizován a rozsáhle dokumentován od UMTS (R99) dále. Motivací bylo zvládnout rostoucí složitost sítí 3G a později 4G/5G, které přinesly mnoho nových síťových entit a rozhraní. Model EP umožňuje přidávat nové funkce definováním nových procedur nebo rozšířením stávajících bez narušení zpětné kompatibility, což podporuje plynulý vývoj mobilních standardů po desetiletí.

## Klíčové vlastnosti

- Definuje kompletní, nedělitelnou signalizační transakci
- Specifikuje sekvence zpráv iniciující a odpovídající strany
- Zahrnuje formální definice pro výsledky úspěchu a selhání
- Rozdělena na procedury třídy 1 (s odpovědí) a třídy 2 (bez odpovědi)
- Používá formální popisné jazyky jako ASN.1 pro jednoznačnou specifikaci
- Tvoří základní stavební prvek všech signalizačních protokolů vyšších vrstev 3GPP

## Související pojmy

- [NGAP – Next Generation Application Protocol](/mobilnisite/slovnik/ngap/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.419** (Rel-19) — Service Area Broadcast Protocol (SABP)
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 25.468** (Rel-19) — RANAP User Adaption (RUA) protocol specification
- **TS 25.469** (Rel-19) — HNBAP Specification for HNB to HNB-GW Interface
- **TS 25.470** (Rel-19) — PCAP User Adaption (PUA) protocol specification
- **TS 25.471** (Rel-19) — RNSAP User Adaptation (RNA) for Iurh
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 26.077** (Rel-19) — AMR Noise Suppression Minimum Performance Requirements
- **TS 29.108** (Rel-19) — RANAP on E-interface for 3G MSC Relocation
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 32.361** (Rel-19) — Entry Point IRP Requirements
- **TS 32.362** (Rel-19) — Entry Point IRP Information Service
- … a dalších 12 specifikací

---

📖 **Anglický originál a plná specifikace:** [EP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ep/)
