---
slug: "cb"
url: "/mobilnisite/slovnik/cb/"
type: "slovnik"
title: "CB – Communication Barring"
date: 2026-01-01
abbr: "CB"
fullName: "Communication Barring"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cb/"
summary: "Communication Barring (CB) je síťová služba, která umožňuje uživatelům nebo operátorům omezit konkrétní typy komunikačních pokusů, například odchozí nebo příchozí hovory a SMS. Poskytuje selektivní ko"
---

CB je síťová služba, která umožňuje uživatelům nebo operátorům omezit konkrétní typy komunikačních pokusů, například odchozí nebo příchozí hovory a SMS.

## Popis

Communication Barring (CB) je standardizovaná doplňková služba v rámci architektury 3GPP, která umožňuje selektivní blokování komunikačních pokusů. Funguje tak, že zachycuje požadavky na navázání relace (např. pro hlasové hovory, videohovory nebo zprávy) a aplikuje předdefinovaná kritéria blokování, než je požadavek předán zamýšlenému příjemci nebo síťovému prvku. Služba je typicky vyvolána v jádru sítě, konkrétně uvnitř funkce Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) v IP Multimedia Subsystem (IMS) pro paketové služby nebo v Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) pro okruhově přepínané služby. Když je iniciován komunikační pokus, obsluhující síťový uzel zkontroluje profil účastníka, který obsahuje aktivní podmínky blokování uložené v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo lokální databázi. Pokud je nalezena shoda, je požadavek odmítnut s konkrétním kódem příčiny a relace není navázána.

Architektura CB zahrnuje několik klíčových komponent: uživatelské zařízení (UE), které může mít nastavení nebo indikace na straně klienta; obsluhující síťový uzel (např. CSCF, MSC), který provádí kontrolu blokování; a úložiště dat o účastníkovi (např. HSS), které uchovává konfigurace blokování. Podmínky blokování mohou být založeny na různých faktorech, včetně typu komunikace (např. odchozí, příchozí), cílového nebo zdrojového čísla (pomocí shody prefixu nebo konkrétních čísel), denní doby nebo polohy účastníka. Například účastník může aktivovat 'Blokování všech odchozích hovorů', aby zabránil zahájení všech hlasových hovorů, nebo 'Blokování příchozích hovorů od anonymních čísel', aby blokoval hovory se skrytým identifikátorem volajícího. Služba podporuje trvalou i dočasnou aktivaci, často spravovanou prostřednictvím USSD kódů, bezdrátové provize (over-the-air provisioning) nebo webového rozhraní.

V síti hraje CB klíčovou roli v řízení provozu a kontrole účastníků. Pro operátory pomáhá předcházet podvodům, řídit síťové přetížení blokováním určitých vzorců hovorů a vynucovat regulatorní požadavky (např. blokování čísel s prémiovou sazbou). Pro koncové uživatele poskytuje nástroje pro ochranu soukromí (např. blokování nevyžádaných hovorů), kontrolu nákladů (např. blokování mezinárodních hovorů) a řízení pozornosti (např. blokování všech hovorů během jednání). Služba je integrována s dalšími mechanismy 3GPP, jako je přesměrování hovorů a bezpodmínečné blokování hovorů, aby vytvářela komplexní servisní logiku. V sítích IMS je CB implementována jako součást Telephony Application Server (TAS) nebo Service Centralization and Continuity Application Server (SCC [AS](/mobilnisite/slovnik/as/)), které provádějí servisní logiku na základě initial Filter Criteria (iFC) stažených z HSS. Z hlediska výkonu jsou kontroly CB navrženy tak, aby měly nízkou latenci a nedocházelo k ovlivnění dob navazování hovorů; typicky zahrnují jednoduché vyhledávání v databázi a porovnávání vzorů.

Vývoj CB zaznamenal její rozšíření od základního blokování v okruhově přepínaných sítích GSM ke komplexnímu blokování založenému na IMS v LTE a 5G. V pozdějších verzích podporuje blokování pro multimediální relace, včetně videohovorů a zasílání zpráv přes IP, a integruje se se službami přítomnosti a lokalizace pro dynamičtější pravidla blokování. Služba také spolupracuje se systémy Lawful Interception ([LI](/mobilnisite/slovnik/li/)), aby zajistila, že blokování nezasahuje do povinného odposlechu. Celkově je CB základní službou, která vyvažuje autonomii uživatele s provozními potřebami sítě, a je implementována prostřednictvím distribuované, na profilech založené architektury napříč jádrem sítě.

## K čemu slouží

Communication Barring (Blokování komunikace) bylo vytvořeno k řešení potřeby kontrolovaného přístupu ke komunikaci v mobilních sítích a řeší problémy související se soukromím, správou nákladů a využitím síťových zdrojů. V raných celulárních systémech, jako je GSM, měli účastníci omezenou možnost omezovat nevyžádané hovory nebo kontrolovat výdaje, což vedlo k problémům, jako je nečekaně vysoký účet z důvodu neautorizovaného použití nebo obtěžujících hovorů. Operátoři také čelili výzvám spojeným s podvodnými aktivitami, jako je krádež předplacené služby nebo podvody s čísly s prémiovou sazbou, které mohly přetížit síťové zdroje. CB poskytlo standardizovaný mechanismus, který umožňuje uživatelům selektivně blokovat komunikační pokusy podle svých preferencí, a zároveň dalo operátorům nástroj k vynucování politik a omezení zneužívání.

Historicky, před zavedením CB, existovaly podobné funkce jako proprietární služby operátorů nebo základní funkce na úrovni ústředny, ale postrádaly interoperabilitu a konzistentní uživatelský zážitek napříč sítěmi. Zavedení CB v 3GPP Release 99 standardizovalo tyto schopnosti, což zajistilo jejich bezproblémové fungování v prostředí s více dodavateli a v roamingu. Vyřešilo omezení předchozích ad-hoc přístupů definováním jasných protokolů pro aktivaci, deaktivaci a dotazování na stav blokování, integrovaných s profilem účastníka v domovské síti. To umožnilo funkce, jako je blokování všech odchozích hovorů při ztrátě telefonu, nebo blokování příchozích hovorů během konkrétních hodin, což zvýšilo jak bezpečnost, tak pohodlí.

V moderních sítích se účel CB rozšířil o podporu komunikace založené na IP v IMS, kde spravuje nejen hlas, ale také video, zasílání zpráv a další multimediální relace. Řeší problémy jako spam přes IP telefonii (SPIT) a neautorizované používání služeb v síťových řezech 5G. Poskytnutím podrobné kontroly – například blokování na základě identity volajícího, typu relace nebo času – pomáhá CB udržovat kvalitu služeb (QoS) a plnit regulatorní požadavky (např. seznamy 'do-not-call'). Její integrace s network slicing v 5G umožňuje operátorům nabízet diferencované politiky blokování na řež, což vyhovuje podnikovým případům použití nebo IoT případům, kde jsou komunikační omezení klíčová pro bezpečnost a provozní efektivitu.

## Klíčové vlastnosti

- Selektivní blokování odchozích/příchozích hlasových a videohovorů
- Blokování SMS a multimediálních zpráv
- Časově a lokalizačně závislá aktivace blokování
- Integrace s profilem účastníka v HSS pro trvalá nastavení
- Podpora odmítnutí anonymních hovorů a blokování konkrétních čísel
- Spolupracuje s přesměrováním hovorů a dalšími doplňkovými službami

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- **TS 24.315** (Rel-19) — Operator Determined Barring (ODB) for IMS
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.411** (Rel-8) — ACR and CB Service Protocol Specification
- **TS 24.416** (Rel-7) — Malicious Call Identification Service
- **TS 24.429** (Rel-7) — Explicit Communication Transfer (ECT) Service Specification
- **TS 24.447** (Rel-8) — Advice Of Charge (AOC) Service Protocol
- **TS 24.504** (Rel-8) — Communication Diversion Services Stage 3
- **TS 24.516** (Rel-8) — MCID Protocol Specification for NGN
- … a dalších 18 specifikací

---

📖 **Anglický originál a plná specifikace:** [CB na 3GPP Explorer](https://3gpp-explorer.com/glossary/cb/)
