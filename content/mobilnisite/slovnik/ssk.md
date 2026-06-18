---
slug: "ssk"
url: "/mobilnisite/slovnik/ssk/"
type: "slovnik"
title: "SSK – Secret Signing Key"
date: 2025-01-01
abbr: "SSK"
fullName: "Secret Signing Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ssk/"
summary: "Kryptografický klíč používaný k vytváření digitálních podpisů pro zajištění integrity a autenticity zpráv v sítích 3GPP. Je klíčovou součástí bezpečnostních protokolů pro ochranu signalizačních a uživ"
---

SSK je kryptografický klíč používaný v sítích 3GPP k vytváření digitálních podpisů pro zajištění integrity a autenticity zpráv, který chrání signalizační a uživatelská data před pozměněním a falšováním.

## Popis

Secret Signing Key (SSK) je symetrický nebo asymetrický kryptografický klíč používaný v bezpečnostních architekturách 3GPP k vytváření digitálních podpisů. Jeho hlavní funkcí je poskytovat autentizaci původu dat a ochranu integrity pro různé síťové zprávy a signalizační procedury. V praxi je SSK typicky generován a bezpečně uložen v rámci síťové entity, jako je Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)), nebo v rámci Universal Integrated Circuit Card (UICC) na straně uživatelského zařízení (UE). Klíč se používá spolu s podpisovým algoritmem (např. založeným na [RSA](/mobilnisite/slovnik/rsa/) nebo [ECC](/mobilnisite/slovnik/ecc/)) k vytvoření podpisu pro konkrétní sadu dat, který může následně ověřit přijímající entita disponující odpovídajícím veřejným klíčem nebo sdíleným tajemstvím.

Architektonická role SSK je často definována v kontextu konkrétních služebních prostředí nebo autentizačních rámců. Například v kontextu vystavení schopností služeb nebo autentizace pro přístup mimo 3GPP může být SSK použit k podepisování tokenů nebo tvrzení. Životní cyklus správy klíče – včetně generování, distribuce, uložení, použití a případného odvolání nebo obnovení – je kritický a je specifikován v příslušných bezpečnostních specifikacích 3GPP, aby se zabránilo jeho kompromitaci. Použití SSK pomáhá vytvořit řetězec důvěry mezi síťovými funkcemi, což zajišťuje, že příkazy nebo autorizační udělení nebyly změněny a pocházejí z legitimního zdroje.

Z provozní perspektivy, když síťová funkce potřebuje potvrdit nárok (např. stav uživatelské autentizace nebo autorizaci služby), použije svůj privátní SSK k vygenerování podpisu nad daty nároku. Tento podepsaný objekt je následně přenesen na konzumující funkci. Spotřebitel, u kterého musí být navázán vztah důvěry (často prostřednictvím předem sdílených veřejných klíčů nebo infrastruktury veřejných klíčů), ověří podpis pomocí odpovídajícího veřejného klíče. Úspěšné ověření potvrdí jak integritu zprávy, tak identitu podepisujícího, což vytváří základ pro bezpečné interakce služeb. Tento mechanismus je zásadní v moderních architekturách založených na službách, kde síťové funkce komunikují přes rozhraní založená na [HTTP](/mobilnisite/slovnik/http/), která mohou procházet méně důvěryhodnými doménami.

## K čemu slouží

SSK byl zaveden, aby řešil rostoucí potřebu robustních bezpečnostních mechanismů v stále otevřenějších a na služby orientovaných architekturách sítí 3GPP. Jak se sítě vyvíjely směrem k cloud-nativním, dekomponovaným funkcím komunikujícím přes [API](/mobilnisite/slovnik/api/), tradiční zabezpečení na úrovni spojení se stalo nedostatečným pro zajištění zpráv end-to-end mezi aplikacemi a síťovými funkcemi. SSK poskytuje standardizovanou metodu pro implementaci digitálních podpisů, která řeší problémy související s pozměňováním zpráv, útoky opakováním a zosobňováním v rámci signalizačních toků.

Historicky se dřívější verze 3GPP více spoléhaly na kryptografické klíče pro šifrování a ochranu integrity v rámci specifických rádiových nebo jádrových síťových protokolů (např. v [NAS](/mobilnisite/slovnik/nas/) nebo [RRC](/mobilnisite/slovnik/rrc/)). Avšak s vystavením síťových schopností aplikacím třetích stran a propojováním různorodých síťových funkcí v 5G vznikla jasná motivace definovat typ klíče explicitně určený pro nepopiratelnost a autentizaci zdroje. SSK tuto mezeru zaplňuje a umožňuje funkce jako bezpečná autorizace služeb, podepsané aktualizace politik a ověřitelné záznamy auditů. Jeho vytvoření bylo motivováno požadavky na důvěryhodnou výměnu dat ve scénářích, jako je síťové dělení (network slicing), edge computing a autentizace napříč heterogenními přístupovými sítěmi, kde musí být původ a integrita řídicích příkazů nebo dat uživatelského kontextu kryptograficky zaručeny.

## Klíčové vlastnosti

- Umožňuje generování digitálních podpisů pro autentizaci původu dat
- Poskytuje kryptografickou ochranu integrity pro signalizační zprávy a uživatelská data
- Může být implementován pomocí symetrické nebo asymetrické kryptografie dle specifikace
- Integruje se s rámci pro správu a ukládání bezpečnostních klíčů 3GPP
- Podporuje služby nepopiratelnosti pro kritické síťové operace
- Používá se v autentizačních a autorizačních protokolech pro vystavení služeb

## Související pojmy

- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 24.582** (Rel-19) — MCData Media Plane Control Protocols
- **TS 33.885** (Rel-14) — Security Study for V2X Services

---

📖 **Anglický originál a plná specifikace:** [SSK na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssk/)
