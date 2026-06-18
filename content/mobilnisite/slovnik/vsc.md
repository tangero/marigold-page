---
slug: "vsc"
url: "/mobilnisite/slovnik/vsc/"
type: "slovnik"
title: "VSC – Videotex Service Centre"
date: 2025-01-01
abbr: "VSC"
fullName: "Videotex Service Centre"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vsc/"
summary: "Videotex Service Centre (VSC) je síťový prvek v zastaralých systémech 3GPP, který poskytuje videotexové služby, ranou formu interaktivního vyhledávání informací využívající text a jednoduchou grafiku"
---

VSC je zastaralý síťový prvek 3GPP, který poskytoval standardizované videotexové služby – raný interaktivní informační systém využívající text a jednoduchou grafiku přenášené po telefonních linkách.

## Popis

Videotex Service Centre (VSC) je v rámci specifikací 3GPP definován jako funkční entita zodpovědná za poskytování videotexových služeb. Videotex byla raná telekomunikační služba umožňující vyhledávání informací prezentovaných jako text nebo základní bloková grafika na terminálu, typicky přes telefonní síť. Architektonicky VSC funguje jako servisní uzel nebo server v síti, který komunikuje s dalšími síťovými prvky za účelem doručení obsahu účastníkům. Spravuje uživatelské relace, zajišťuje ukládání a načítání informačních stránek a formátuje data pro zobrazení na kompatibilních terminálech. Provoz VSC zahrnuje navázání spojení s uživatelským terminálem, v případě potřeby autentizaci uživatele a následné zprostředkování interaktivního výběru a přenosu informačních rámců. Mezi klíčové komponenty patří databáze ukládající informační stránky, logika správy relací a adaptační funkce potřebné pro komunikaci se signalizačními a přenosovými schopnostmi mobilní sítě. Jeho úlohou bylo být centrálním bodem pro nabízení standardizovaných, sítí poskytovaných informačních služeb, které mohly zahrnovat zprávy, počasí, bankovnictví nebo vyhledávání v adresářích, v době před nástupem webu.

Co se týče technické implementace, VSC využíval specifické protokoly pro komunikaci. Zatímco základní specifikace 3GPP (jako 21.905 pro slovník a 23.043 pro technickou realizaci) definují jeho roli a požadavky, samotný přenos dat by spoléhal na okruhově spínané datové přenosy nebo specifické signalizační protokoly dostupné v sítích GSM a raných sítích UMTS. Servisní logika uvnitř VSC řídila uživatelský dialog a navigaci přes stromovou strukturu menu stránek. Každá stránka, identifikovaná číslem, obsahovala informace k zobrazení. VSC byl klíčovou součástí ekosystému služeb s přidanou hodnotou ([VAS](/mobilnisite/slovnik/vas/)) před rozšířením paketově spínaných internetových protokolů.

Význam VSC spočívá v jeho historické pozici jako standardizovaného pokusu přinést interaktivní datové služby masovému mobilnímu trhu. Představoval krok za hranice jednoduchého hlasu a [SMS](/mobilnisite/slovnik/sms/) a zkoumal, jak mohou sítě doručovat strukturované informace. Zatímco samotná specifická technologie videotexu zastarala s nástupem World Wide Web a mobilního internetu (služby [GPRS](/mobilnisite/slovnik/gprs/), paketové služby UMTS), architektonický koncept specializovaného servisního centra pro hostování a doručování obsahu připravil cestu pro pozdější servisní platformy, jako jsou Multimedia Messaging Service Centres (MMSC) a různé aplikační servery v sítích založených na IMS.

## K čemu slouží

VSC byl vytvořen za účelem standardizace a umožnění videotexových služeb v mobilních sítích 3GPP. Videotex byla populární informační služba ve světě pevných telefonních linek (známá jako Prestel ve Velké Británii, Minitel ve Francii atd.) a existovala snaha rozšířit podobné možnosti interaktivního textového vyhledávání informací i na mobilní účastníky. Problém, který řešil, byl nedostatek standardizovaného, sítí poskytovaného mechanismu pro doručování interaktivních informačních služeb na raných digitálních celulárních sítích, jako je GSM. Před takovou standardizací by bylo nabízení těchto služeb proprietární a fragmentované napříč různými operátory a regiony.

Motivace vycházela z komerční potřeby zvýšit průměrný výnos na uživatele ([ARPU](/mobilnisite/slovnik/arpu/)) nabízením služeb s přidanou hodnotou nad rámec základního hlasu. Řešila omezení jednoduché [SMS](/mobilnisite/slovnik/sms/), která byla službou přenosu zpráv mezi osobami, tím, že poskytovala strukturovaný, na serveru založený model přístupu k informacím. Specifikace VSC poskytovala společný rámec pro výrobce síťového vybavení a poskytovatele služeb, zajišťovala interoperabilitu a podporovala vznik servisního ekosystému. Byla součástí širších snah o standardizaci GSM fáze 2+ zaměřených na vylepšení možností datových služeb.

Historicky byl účel VSC nakonec překonán evolucí směrem k univerzálním paketovým datovým sítím. Nástup [GPRS](/mobilnisite/slovnik/gprs/) a později 3G/UMTS s neustálým IP připojením učinil okruhově spínaný, na terminálu specifický model videotexu méně atraktivním ve srovnání s flexibilitou webového prohlížení a IP aplikací. Avšak ve své době představoval důležitý krok v konceptuální evoluci mobilních datových služeb.

## Klíčové vlastnosti

- Standardizované rozhraní pro poskytování videotexové služby
- Správa interaktivních uživatelských relací pro vyhledávání informací
- Ukládání a poskytování strukturovaných informačních stránek (text/grafika)
- Podpora protokolů pro navigaci v menu a výběr stránek
- Integrace se signalizací mobilní sítě pro přístup ke službě
- Definován jako součást rámce služeb s přidanou hodnotou (VAS) 3GPP

## Související pojmy

- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)
- [USSD – Unstructured Supplementary Services Data](/mobilnisite/slovnik/ussd/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.043** (Rel-4) — GSM Videotex Service Support

---

📖 **Anglický originál a plná specifikace:** [VSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/vsc/)
