---
slug: "mmsr-s"
url: "/mobilnisite/slovnik/mmsr-s/"
type: "slovnik"
title: "MMSR/S – Multimedia Messaging Relay/Server"
date: 2025-01-01
abbr: "MMSR/S"
fullName: "Multimedia Messaging Relay/Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mmsr-s/"
summary: "Multimedia Messaging Relay/Server (MMSR/S) je kombinovaný síťový prvek, který plní funkce přenosového uzlu i serveru pro službu Multimedia Messaging Service (MMS). Zajišťuje směrování, ukládání a prop"
---

MMSR/S je kombinovaný síťový prvek v rané architektuře MMS, který plní funkce jak přenosového uzlu (relay), tak serveru pro zpracování směrování, ukládání a propojování multimediálních zpráv.

## Popis

Multimedia Messaging Relay/Server ([MMSR](/mobilnisite/slovnik/mmsr/)/S) je funkční síťová entita definovaná v raných vydáních 3GPP, která kombinuje schopnosti Multimedia Messaging Service Relay ([MMS](/mobilnisite/slovnik/mms/) Relay) a Multimedia Messaging Service Server (MMS Server). V architektuře MMS jsou tyto funkce často konceptualizovány odděleně: MMS Relay zajišťuje převod protokolů a přenos zpráv mezi různými sítěmi (např. mezi mobilní sítí a internetem), zatímco MMS Server poskytuje logiku ukládání a zpracování, jako je správa uživatelských profilů a indikací čekajících zpráv. MMSR/S představuje integrovanou implementaci těchto dvou logických funkcí v rámci jednoho fyzického nebo logického síťového uzlu.

Provozně funguje MMSR/S jako centrální uzel pro provoz MMS. Když uživatel odešle MMS, uživatelský agent MMS (MMS [UA](/mobilnisite/slovnik/ua/)) předá zprávu MMSR/S. MMSR/S poté zprávu uloží, identifikuje příjemce a určí optimální trasu pro doručení. Pokud je příjemce ve stejné síti, může zprávu přeposlat přímo. Pokud je příjemce v jiné síti (např. u jiného mobilního operátora nebo na emailovém serveru), MMSR/S provede potřebné propojení a adaptaci protokolů. Používá standardizovaná rozhraní jako MM1 (mezi UA a [MMSE](/mobilnisite/slovnik/mmse/)), MM3 (k externím serverům) a MM4 (k jiným MMSE). Serverová komponenta spravuje funkce jako vypršení platnosti zprávy, generování účtovacích dat a hlášení o doručení.

Klíčové vnitřní komponenty zahrnují úložiště zpráv, funkci pro propojování ([IWF](/mobilnisite/slovnik/iwf/)), směrovací engine a rozhraní k účtovací bráně. MMSR/S musí podporovat vysokou dostupnost a škálovatelnost, aby zvládal velké objemy multimediálního obsahu. Jeho integrovaný návrh zjednodušil raná nasazení MMS snížením počtu potřebných diskrétních síťových prvků, ačkoli pozdější architektury tyto funkce často oddělily pro větší flexibilitu a škálovatelnost.

## K čemu slouží

[MMSR](/mobilnisite/slovnik/mmsr/)/S byl specifikován, aby poskytl konkrétní, implementovatelný síťový prvek pro raná nasazení služby Multimedia Messaging Service ([MMS](/mobilnisite/slovnik/mms/)). Když se MMS vyvíjela z konceptu na komerční službu, potřebovali síťoví operátoři jasný plán pro základní infrastrukturu. Definice kombinované entity Relay/Server nabídla praktické řešení, které v jednom systému zahrnulo nezbytné funkce ukládání a přeposílání (store-and-forward) a brány (gateway). Tím se snížila složitost implementace a urychlil se čas uvedení prvních MMS nabídek na trh.

Řešila potřebu centrálního uzlu, který by mohl komunikovat jak s mobilním paketovým jádrem (např. přes GGSN), tak s externími messagingovými systémy, jako je email nebo starší centra [SMS](/mobilnisite/slovnik/sms/). Integrovaný MMSR/S řešil kritický problém interoperability – převod mezi protokoly založenými na WAP nebo HTTP používanými v mobilní doméně a protokoly jako SMTP používanými externě. Kombinací funkcí relay a serveru zajišťoval konzistentní zpracování zpráv, účtování a správu účastníků z jednoho kontrolního bodu. Tento model byl obzvláště vhodný pro počáteční fázi MMS, kdy byl rozsah služeb a sada funkcí omezenější.

## Klíčové vlastnosti

- Kombinuje funkce směrování/propojování zpráv MMS Relay s funkcemi ukládání a servisní logiky MMS Serveru
- Poskytuje funkci ukládání a přeposílání (store-and-forward) pro multimediální zprávy, zajišťující doručení i v případě, že je příjemce offline
- Provádí převod a adaptaci protokolů pro propojení s externími messagingovými systémy (např. email, jiní poskytovatelé MMS)
- Generuje záznamy o účtovacích datech (CDR) pro účely fakturace podle specifikací 3GPP
- Spravuje vypršení platnosti zpráv, hlášení o doručení a hlášení o přečtení/odpovědích
- Podporuje standardizovaná rozhraní (MM1, MM3, MM4) pro komunikaci s uživatelskými agenty a dalšími síťovými prvky

## Související pojmy

- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)
- [CDR – Call Detail Record](/mobilnisite/slovnik/cdr/)

## Definující specifikace

- **TS 32.270** (Rel-19) — MMS Charging Management Specification
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)

---

📖 **Anglický originál a plná specifikace:** [MMSR/S na 3GPP Explorer](https://3gpp-explorer.com/glossary/mmsr-s/)
