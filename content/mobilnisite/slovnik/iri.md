---
slug: "iri"
url: "/mobilnisite/slovnik/iri/"
type: "slovnik"
title: "IRI – Intercept Related Information"
date: 2025-01-01
abbr: "IRI"
fullName: "Intercept Related Information"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/iri/"
summary: "IRI jsou metadata a informace spojené s hovorem shromažďované při zákonném odposlechu telekomunikací. Zahrnují podrobnosti jako identity, polohu a časová razítka, odděleně od vlastního obsahu komunika"
---

IRI jsou metadata a informace spojené s hovorem, jako jsou identity, poloha a časová razítka, shromažďované při zákonném odposlechu telekomunikací, odděleně od vlastního obsahu komunikace.

## Popis

Intercept Related Information (IRI) je klíčová součást architektury zákonného odposlechu ([LI](/mobilnisite/slovnik/li/)) standardizované organizací 3GPP. Představuje soubor informací nebo dat spojených s telekomunikačními službami cílového účastníka, s výjimkou vlastního obsahu komunikace. IRI generují síťové funkce jako Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)), Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) nebo Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) a jsou doručovány zařízení pro monitorování orgánů činných v trestním řízení ([LEMF](/mobilnisite/slovnik/lemf/)) prostřednictvím mediační funkce ([MF](/mobilnisite/slovnik/mf/)). Datový proud IRI je oddělen od proudu obsahu komunikace ([CC](/mobilnisite/slovnik/cc/)), což zajišťuje jasné rozlišení mezi metadaty hovoru a vlastní hlasovou nebo datovou přenosovou jednotkou.

Architektonicky je IRI definováno v rámci rozhraní předání ([HI](/mobilnisite/slovnik/hi/)) mezi doménou síťového operátora a doménou orgánů činných v trestním řízení. Generování IRI je spouštěno příkazy k odposlechu a je založeno na událostech v síti týkajících se cílového účastníka. Mezi klíčové síťové prvky zapojené do tohoto procesu patří řídicí prvek provádějící odposlech (ICE), který detekuje aktivitu cíle a generuje nezpracovaná IRI data, a mediační funkce, která tato data formátuje a doručuje podle standardizovaných protokolů, jako jsou standardy ETSI nebo specifikace 3GPP ATIS/T1. LI. Doručení využívá spolehlivé transportní mechanismy, aby byla zajištěna integrita a autenticita odposlechnutých dat.

Informace obsažené v IRI jsou rozsáhlé a standardizované. Typicky zahrnují identitu odposlechnutého cíle (např. IMSI, MSISDN), identitu komunikující strany, polohu cíle (Cell ID, TAI nebo přesnější polohu, je-li dostupná), čas a datum komunikační události, typ komunikační služby (např. hlasový hovor, SMS, paketová datová relace) a směr komunikace. U datových relací může IRI zahrnovat podrobnosti jako aktivace PDP kontextu, použité APN a přidělené IP adresy. Tato metadata poskytují kontext nezbytný pro orgány činné v trestním řízení, aby pochopily „kdo, kdy, kde a jak“ komunikace, aniž by zpočátku přistupovaly k soukromému obsahu, a dodržují tak právní zásady přiměřenosti.

IRI hraje zásadní roli při zajišťování toho, aby síťoví operátoři mohli standardizovaným, bezpečným a efektivním způsobem plnit národní zákonné požadavky na zákonný odposlech. Jeho striktní oddělení od CC usnadňuje kontrolovaný přístup a auditování. Standardizace parametrů IRI napříč vydáními 3GPP zajišťuje interoperabilitu mezi zařízeními od různých dodavatelů a konzistentní prezentaci dat orgánům činným v trestním řízení po celém světě, což je klíčové pro nadnárodní vyšetřování a shodu operátorů s předpisy.

## K čemu slouží

IRI existuje za účelem plnění zákonných povinností ukládaných poskytovatelům telekomunikačních služeb, aby pomáhaly orgánům činným v trestním řízení a bezpečnostním složkám v trestních vyšetřováních a záležitostech národní bezpečnosti. Zákony ve většině zemí ukládají síťovým operátorům povinnost mít technickou schopnost odposlouchávat komunikaci při předložení zákonného příkazu. Před standardizací vytvářely proprietární a nekompatibilní systémy odposlechu významné výzvy pro operátory s více dodavatelskými sítěmi a pro orgány činné v trestním řízení, které potřebovaly zpracovávat data od různých operátorů.

Vytvoření standardizovaného IRI jako součásti širšího rámce zákonného odposlechu 3GPP řeší problém interoperability a nákladů. Definuje jednotnou sadu metadat, která musí být poskytnuta bez ohledu na technologii základního síťového dodavatele. To umožňuje orgánům činným v trestním řízení přijímat informace ve konzistentním formátu, což zjednodušuje jejich monitorovací nástroje a postupy. Také snižuje náklady na vývoj a integraci pro výrobce síťového zařízení a operátory, protože mohou implementovat jediné, dobře definované rozhraní.

Oddělení IRI od CC navíc řeší obavy související se soukromím a právními aspekty tím, že umožňuje stupňovaný přístup k odposlechu. Orgány mohou zpočátku přijímat pouze kontextová metadata (IRI) ke zjištění skutečností a k více invazivnímu obsahu komunikace (CC) přistupovat pouze tehdy, když je to konkrétně odůvodněno. Tento architektonický princip podporuje právní zásadu přiměřenosti. Vývoj IRI napříč vydáními 3GPP byl poháněn novými službami (VoLTE, VoWiFi, 5G) a potřebou zahrnout nové typy metadat, jako jsou identity IMS, indikátory domény služeb a vylepšené informace o poloze, což zajišťuje, že schopnost odposlechu zůstává účinná v moderních sítích založených na IP.

## Klíčové vlastnosti

- Standardizovaná sada metadat zahrnující identitu cíle, komunikující stranu a typ služby
- Samostatný doručovací proud oddělený od obsahu komunikace (CC) pro kontrolovaný přístup
- Generováno síťovými řídicími prvky (ICE), jako jsou MME, SGSN nebo S-CSCF
- Doručováno prostřednictvím mediační funkce přes standardizované rozhraní předání (HI)
- Obsahuje kritické informace o poloze (např. Cell ID, Tracking Area)
- Podporuje události pro služby s přepojováním okruhů, přepojováním paketů a služby založené na IMS

## Definující specifikace

- **TS 33.106** (Rel-19) — Lawful Interception Requirements (Pre-Rel-15)
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 33.126** (Rel-19) — Lawful Interception Requirements
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols
- **TS 43.033** (Rel-13) — Lawful Interception Stage 2 for GSM/GPRS

---

📖 **Anglický originál a plná specifikace:** [IRI na 3GPP Explorer](https://3gpp-explorer.com/glossary/iri/)
