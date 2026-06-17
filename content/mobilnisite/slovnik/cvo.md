---
slug: "cvo"
url: "/mobilnisite/slovnik/cvo/"
type: "slovnik"
title: "CVO – Coordination of Video Orientation"
date: 2025-01-01
abbr: "CVO"
fullName: "Coordination of Video Orientation"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cvo/"
summary: "CVO je služba 3GPP, která synchronizuje orientaci videa mezi vysílajícím a přijímajícím zařízením během videohovorů. Zajišťuje správnou orientaci zobrazení bez ohledu na rotaci zařízení, čímž předcház"
---

CVO je služba 3GPP, která synchronizuje orientaci videa mezi zařízeními během hovoru, aby zajistila správné zobrazení bez ohledu na rotaci zařízení, a zabrání tak převrácenému nebo bočně orientovanému videu.

## Popis

Coordination of Video Orientation (CVO) je standardizovaný mechanismus v rámci multimediálních telefonních služeb 3GPP, který řeší problém udržení správné orientace videa během relací komunikace v reálném čase. Když se zařízení během videohovoru otáčí, CVO zajišťuje, aby byl přenášený video stream správně orientován na displeji přijímacího zařízení, a předchází tak běžnému problému převráceného nebo bočně orientovaného zobrazení videa, který nastává, když nejsou senzory orientace zařízení mezi koncovými body řádně koordinovány.

Technická implementace CVO funguje prostřednictvím signalizačních protokolů, které si vyměňují informace o orientaci mezi uživatelským zařízením (UE) a síťovými elementy. Když se zařízení otočí, jeho senzory orientace změnu detekují a mechanismus CVO vygeneruje signalizační zprávy obsahující metadata o orientaci. Tyto informace jsou přenášeny přes jádrovou síť IP Multimedia Subsystem (IMS) s využitím rozšíření protokolu Session Initiation Protocol (SIP) a rozšíření hlaviček protokolu Real-time Transport Protocol (RTP). Přijímací zařízení tato data o orientaci zpracuje a aplikuje příslušnou rotaci na video stream před jeho vykreslením na displeji.

Z architektonického hlediska se na CVO podílí více síťových komponent včetně UE, elementů jádra IMS ([P-CSCF](/mobilnisite/slovnik/p-cscf/), S-CSCF) a funkcí pro zpracování médií. UE implementuje klientskou funkcionalitu CVO, která monitoruje senzory orientace zařízení a generuje odpovídající signalizaci. Síť IMS směruje signalizační zprávy CVO mezi koncovými body při zachování kontinuity relace. Mediální brány a funkce mediálních zdrojů se mohou na zpracování CVO také podílet, když je mezi různými kodeky nebo síťovými podmínkami vyžadován překód nebo adaptace médií.

CVO funguje v součinnosti se stávajícími videokodeky a transportními protokoly, aniž by vyžadovalo úpravy základních procesů kódování/dekódování videa. Informace o orientaci jsou přenášeny jako metadata oddělená od zakódované video datové části, což umožňuje zpětnou kompatibilitu se zařízeními, která CVO nepodporují. Mechanismus podporuje dynamické změny orientace během aktivních relací s minimální latencí, aby zajistil plynulé přechody, když uživatelé otáčejí svá zařízení. Tato koordinace je zvláště důležitá pro mobilní zařízení, která během videohovorů často mění orientaci mezi režimem na výšku a na šířku.

## K čemu slouží

CVO bylo vytvořeno, aby vyřešilo zásadní problém uživatelského zážitku spojený s nesprávnou orientací videa během mobilních videohovorů. Před standardizací CVO často videotelefonní aplikace zobrazovaly převrácené nebo bočně orientované video, když jeden účastník otočil své zařízení, což vyžadovalo manuální zásah nebo způsobovalo zmatení. Tento problém nabýval na významu s rozšířením chytrých telefonů s automatickou rotací obrazovky a s očekáváním uživatelů, že videokomunikace bude bezproblémová bez ohledu na orientaci zařízení.

Tato technologie řeší omezení dřívějších systémů videokomunikace, kde bylo zacházení s orientací buď neexistující, nebo implementované prostřednictvím proprietárních, neinteroperabilních řešení. Předchozí přístupy často spoléhaly na implementace specifické pro dané zařízení, které nekoordinovaly zařízení různých výrobců, což vedlo k nekonzistentnímu chování napříč sítěmi. Některá raná řešení se pokoušela řešit orientaci prostřednictvím rotace při videokódování, což zvyšovalo procesní režii a degradovalo kvalitu videa zbytečným překódováním.

CVO poskytuje standardizované řešení s podporou sítě, které funguje napříč různými výrobci zařízení a síťovými operátory. Umožňuje konzistentní zacházení s orientací ve službách videotelefonie založených na IMS, včetně videohovorů Voice over LTE (VoLTE) a Voice over Wi-Fi (VoWiFi). Standardizace zajišťuje interoperabilitu v prostředích s více dodavateli a podporuje regulatorní požadavky na nouzové videohovory, kde může být správná orientace klíčová pro přehled o situaci. Oddělením signalizace orientace od videokódování CVO zachovává kvalitu videa a zároveň poskytuje spolehlivou koordinaci orientace.

## Klíčové vlastnosti

- Dynamická synchronizace orientace během aktivních video relací
- Signalizace založená na SIP pro výměnu metadat o orientaci
- Podpora rozšíření hlaviček RTP pro aktualizace orientace v reálném čase
- Zpětná kompatibilita se zařízeními nepodporujícími CVO
- Podpora režimů orientace na výšku i na šířku
- Zpracování přechodů orientace s nízkou latencí

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.244** (Rel-19) — 3GPP File Format (3GP) Specification
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [CVO na 3GPP Explorer](https://3gpp-explorer.com/glossary/cvo/)
