---
slug: "figs"
url: "/mobilnisite/slovnik/figs/"
type: "slovnik"
title: "FIGS – Fraud Information Gathering System"
date: 2025-01-01
abbr: "FIGS"
fullName: "Fraud Information Gathering System"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/figs/"
summary: "Standardizovaný systém pro sběr, výměnu a analýzu informací souvisejících s podvody mezi operátory mobilních sítí a finančními institucemi. Umožňuje odhalování a prevenci podvodů při registraci (subsc"
---

FIGS je standardizovaný systém pro sběr, výměnu a analýzu informací souvisejících s podvody mezi mobilními operátory a finančními institucemi za účelem odhalování a prevence podvodů spojených s registrací a platbami.

## Popis

Fraud Information Gathering System (FIGS) je rámec definovaný organizací 3GPP pro boj proti podvodům v mobilních sítích. Nejde o jeden fyzický systém, ale o soubor specifikací definujících datové modely, rozhraní a postupy pro sdílení informací o podvodech. Základním konceptem jsou záznamy o podvodech (Fraud Information Records, FIRs), což jsou standardizované hlášení obsahující podrobnosti o podezřelých nebo potvrzených podvodných událostech, jako je podvodná registrace (využití ukradené identity), platební podvod nebo technický podvod (např. nabourání se do [PBX](/mobilnisite/slovnik/pbx/)). Tyto FIRs jsou vyměňovány mezi účastnícími se subjekty, typicky prostřednictvím centrálního uzlu nebo přímo mezi operátory.

Z architektonického hlediska implementace FIGS zahrnuje několik klíčových komponent: systémy pro detekci podvodů (Fraud Detection Systems, [FDS](/mobilnisite/slovnik/fds/)) v síti operátora, které generují FIRs na základě analyzovaných vzorců; databázi nebo úložiště FIGS, které tyto záznamy ukládá a spravuje; a rozhraní (často založená na standardizovaných formátech jako X.500/[LDAP](/mobilnisite/slovnik/ldap/) nebo webové služby) pro zabezpečené dotazování a výměnu. Proces funguje tak, že FDS operátora detekuje anomálii – například novou registraci s neobvyklými volacími vzorci odpovídajícími známým charakteristikám podvodu. Vytvoří [FIR](/mobilnisite/slovnik/fir/) podrobně popisující zapojené identity ([MSISDN](/mobilnisite/slovnik/msisdn/), [IMSI](/mobilnisite/slovnik/imsi/)), zařízení ([IMEI](/mobilnisite/slovnik/imei/)), události a typ podvodu. Tento FIR může být sdílen s komunitou FIGS.

Ostatní operátoři pak mohou proaktivně dotazovat databázi FIGS při provádění hodnocení rizik, například při kontrole bonity nového zákazníka nebo při pozorování podezřelé aktivity od roamujícího účastníka. Shoda se známým FIR může spustit zvýšenou kontrolu nebo zamítnutí služby. Úlohou systému je vytvořit kolektivní obranu sdružováním informací o podvodech, což dramaticky zkracuje dobu, za kterou je podvodný vzorec detekovaný v jedné síti rozpoznán a blokován v jiné. Systém funguje přes administrativní hranice, podporuje národní i mezinárodní iniciativy prevence podvodů a úzce souvisí se systémy jako je Equipment Identity Register ([EIR](/mobilnisite/slovnik/eir/)) pro sledování odcizených zařízení.

## K čemu slouží

FIGS byl vytvořen pro řešení významných a rostoucích finančních ztrát způsobených telekomunikačními podvody, které se staly složitějšími s globalizací roamingu a digitálních služeb. Před jeho standardizací se operátoři spoléhali na interní, proprietární systémy pro správu podvodů a bilaterální dohody pro sdílení informací. Tento přístup byl pomalý, neefektivní a nedokázal držet krok s podvodníky, kteří rychle přesouvali své aktivity přes hranice operátorů. Existovala kritická potřeba společného, automatizovaného jazyka a procesu pro sdílení informací o podvodech.

Jeho zavedení v 3GPP Release 4 bylo motivováno nárůstem GSM roamingových podvodů a podvodů při registraci. Systém řeší problém informační asymetrie mezi podvodníkem (který může útočit na více sítí) a jednotlivými operátory (kteří vidí pouze fragment celkové aktivity). Tím, že umožňuje rychlou, standardizovanou výměnu dat o podvodech, umožňuje FIGS operátorovi využít kolektivní zkušenosti celé komunity. Tím se zabrání tomu, aby se podvod po odhalení jednoduše přesunul z jedné sítě do druhé.

Vývoj FIGS byl poháněn novými typy podvodů, jako je SMS phishing (smishing), IRSF (International Revenue Share Fraud) a podvody spojené s IoT registracemi. Poskytuje základní rámec, který se přizpůsobuje novým hrozbám rozšiřováním datového modelu FIR. Účel přesahuje přímou prevenci ztrát; systém také chrání pověst značky, udržuje kvalitu služeb pro legitimní uživatele a podporuje požadavky regulatorní shody související s bezpečností a finanční kriminalitou. Je klíčovou součástí kolektivního bezpečnostního postoje telekomunikačního průmyslu.

## Klíčové vlastnosti

- Standardizovaný formát záznamu o podvodu (Fraud Information Record, FIR) pro konzistentní výměnu dat
- Podpora více typů podvodů včetně podvodů při registraci, platebních a technických podvodů
- Umožňuje proaktivní dotazy i reaktivní varování mezi účastnícími se subjekty
- Usnadňuje spolupráci mezi operátory a přes hranice států v boji proti podvodům
- Integruje se s interními systémy pro detekci podvodů (Fraud Detection Systems, FDS) operátora
- Poskytuje datové modely pro identity související s podvody (MSISDN, IMSI, IMEI, IP adresy)

## Související pojmy

- [EIR – Equipment Identity Register](/mobilnisite/slovnik/eir/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TS 22.031** (Rel-19) — Fraud Information Gathering System (FIGS) Stage 1
- **TS 22.032** (Rel-19) — Immediate Service Termination (IST) Service
- **TS 23.031** (Rel-19) — Fraud Information Gathering System (FIGS) - Stage 2
- **TS 23.035** (Rel-19) — Immediate Service Termination (IST) Stage 2
- **TS 41.031** (Rel-19) — Fraud Information Gathering System (FIGS) Requirements

---

📖 **Anglický originál a plná specifikace:** [FIGS na 3GPP Explorer](https://3gpp-explorer.com/glossary/figs/)
