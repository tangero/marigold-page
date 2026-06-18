---
slug: "cfb"
url: "/mobilnisite/slovnik/cfb/"
type: "slovnik"
title: "CFB – Call Forwarding on mobile subscriber Busy"
date: 2026-01-01
abbr: "CFB"
fullName: "Call Forwarding on mobile subscriber Busy"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cfb/"
summary: "CFB je doplňková služba, která přesměruje příchozí hovory na jiné číslo, když je volaný mobilní účastník obsazen. Zajišťuje, že volající se mohou dovolat na alternativní cíl, místo aby slyšeli obsazen"
---

CFB je doplňková služba, která přesměruje příchozí hovory na jiné číslo, když je volaný mobilní účastník obsazen.

## Popis

Call Forwarding on mobile subscriber Busy (CFB) je základní doplňková služba v architektuře 3GPP, která funguje na úrovni jádra sítě, konkrétně v rámci Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) a Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo řídicích funkcí relace v IP Multimedia Subsystem (IMS). Když dorazí příchozí hovor pro účastníka, který má aktivovanou službu CFB a jehož linka je právě obsazena v jiném hovoru, síť detekuje stav obsazení prostřednictvím monitorování stavu hovoru na MSC serveru nebo telephony application serveru. Servisní logika pak zachytí pokus o sestavení hovoru a přesměruje jej na předem nakonfigurované číslo pro přesměrování uložené v HLR nebo v profilu účastníka na Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). K tomuto přesměrování dojde ještě předtím, než volající uslyší jakoukoliv zvukovou signalizaci, což vytváří plynulý přechod.

Technická implementace zahrnuje několik klíčových signalizačních protokolů. V sítích s přepojováním okruhů služba využívá signalizaci Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)) mezi HLR a MSC/[VLR](/mobilnisite/slovnik/vlr/) k získání a ověření informací o přesměrování. Když je detekován stav obsazení, MSC vygeneruje zprávu MAP_SEND_ROUTING_INFORMATION_FOR_[SM](/mobilnisite/slovnik/sm/) nebo ekvivalentní, aby získalo cíl přesměrování. V sítích založených na IMS je CFB implementována pomocí [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol), kde Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) vyhodnotí počáteční filtrační kritéria a vyvolá logiku aplikačního serveru, když stav registrace volané strany indikuje obsazení. S-CSCF pak upraví SIP INVITE požadavek, aby přesměroval na adresu pro přesměrování.

CFB interaguje s dalšími variantami přesměrování hovorů prostřednictvím hierarchie priority definované ve specifikacích 3GPP. Když existuje více podmínek přesměrování současně (například CFB spolu s Call Forwarding Unconditional nebo Call Forwarding No Reply), síť dodržuje standardizovaná pravidla pro řešení konfliktů. Služba podporuje jak základní přesměrování na jedno číslo, tak pokročilejší scénáře, jako je sekvenční přesměrování, kdy lze vyzkoušet více čísel. Aktivace a deaktivace probíhá prostřednictvím USSD kódů, řídicích procedur doplňkových služeb nebo přes webová rozhraní, přičemž stav je trvale uložen v síťové databázi.

Z pohledu síťové architektury vyžaduje CFB těsnou integraci mezi funkcemi řízení hovorů a správou dat účastníků. MSC nebo CSCF musí mít přístup k aktuálnímu stavu obsazení účastníka v reálném čase a současně konzultovat konfigurační data pro přesměrování. To vytváří distribuovanou servisní logiku, která se rozprostírá přes více síťových prvků, při zachování časových požadavků na sestavení hovoru. Z hlediska výkonu je třeba minimalizovat dodatečnou latenci zavedenou procesem rozhodování o přesměrování a zajistit, aby informace o přesměrování zůstaly aktuální i přes pohyb účastníka mezi lokalizačními oblastmi nebo sledovacími oblastmi.

## K čemu slouží

CFB byla vytvořena, aby vyřešila základní omezení tradiční telefonie, kdy volající slyšeli obsazený tón, když byl volaný účastník zapojen do jiného hovoru, což vedlo k promarněným příležitostem ke komunikaci a neefektivním pokusům o dovolání. Před zavedením služeb přesměrování hovorů neměli mobilní účastníci způsob, jak zajistit, že se k nim důležité hovory dostanou nebo k alternativnímu kontaktu, když nebyli dostupní. To bylo obzvláště problematické v obchodním kontextu, kde zmeškané hovory mohly znamenat ztracené příležitosti nebo opožděné rozhodování.

Služba vznikla jako součást rámce doplňkových služeb GSM v raných vydáních 3GPP, navazovala na podobné koncepty z pevné telefonie, ale byla přizpůsobena pro mobilní prostředí s jedinečnými výzvami, jako je pohyblivost účastníků a různé síťové podmínky. CFB vyřešila problém kontinuity komunikace tím, že poskytla systematický způsob přesměrování hovorů na základě konkrétních podmínek, což uživatelům umožnilo zachovat dostupnost i během období nedostupnosti. To bylo zvláště cenné v éře hlasu s přepojováním okruhů, kdy byly alternativní způsoby komunikace ve srovnání s dnešními multimodálními možnostmi zasílání zpráv omezené.

Nad rámec osobního pohodlí podporovala CFB provozní požadavky organizací, které potřebovaly udržovat kanály kontaktu se zákazníky. Umožňovala směrování přetížení kontaktních center, screening asistentů vedení a základní distribuci hovorů bez nutnosti složitých PBX systémů. Služba také vytvořila základ pro pokročilejší funkce obsluhy hovorů, které se vyvinuly v pozdějších vydáních 3GPP, a stanovila architektonické vzory pro podmíněné směrování hovorů, které byly později rozšířeny na implementace IMS a VoLTE/VoNR.

## Klíčové vlastnosti

- Podmíněné přesměrování hovoru na základě stavu obsazení volané strany
- Implementace na síťové úrovni nevyžadující speciální schopnosti telefonu
- Konfigurovatelné cílové číslo pro přesměrování uložené v HLR/HSS
- Integrace s dalšími doplňkovými službami prostřednictvím standardizovaných pravidel priority
- Podpora pro architektury sítí s přepojováním okruhů i založené na IMS
- Vyvolání v reálném čase na základě monitorování stavu hovoru na MSC nebo CSCF

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 24.416** (Rel-7) — Malicious Call Identification Service
- **TS 24.447** (Rel-8) — Advice Of Charge (AOC) Service Protocol
- **TS 24.504** (Rel-8) — Communication Diversion Services Stage 3
- **TS 24.516** (Rel-8) — MCID Protocol Specification for NGN
- **TS 24.604** (Rel-19) — Communications Diversion (CDIV) Protocol Spec
- **TS 24.606** (Rel-19) — MWI Service Protocol Description
- **TS 24.615** (Rel-19) — Communication Waiting (CW) Service Protocol
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [CFB na 3GPP Explorer](https://3gpp-explorer.com/glossary/cfb/)
