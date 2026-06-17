---
slug: "clip"
url: "/mobilnisite/slovnik/clip/"
type: "slovnik"
title: "CLIP – Calling Line Identification Presentation"
date: 2025-01-01
abbr: "CLIP"
fullName: "Calling Line Identification Presentation"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/clip/"
summary: "CLIP je doplňková služba v sítích 3GPP, která zobrazuje telefonní číslo volajícího straně volané před přijetím hovoru. Umožňuje třídění hovorů, zlepšuje uživatelský komfort a podporuje služby jako zpě"
---

CLIP je doplňková služba v sítích 3GPP, která zobrazuje telefonní číslo volajícího straně volané ještě před přijetím hovoru.

## Popis

Calling Line Identification Presentation (CLIP) je standardizovaná doplňková služba v rámci specifikací 3GPP, která umožňuje síti prezentovat číslo volajícího (nebo jinou identifikaci) koncovému zařízení volaného účastníka. Z architektonického hlediska CLIP funguje uvnitř core sítě, konkrétně využívá možnosti Intelligent Network ([IN](/mobilnisite/slovnik/in/)) a Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) pro data o předplatném služby. Servisní logika je typicky prováděna v Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo v IP Multimedia Subsystem (IMS) pro novější verze, kde zpracovává signalizační zprávy jako Initial Address Message ([IAM](/mobilnisite/slovnik/iam/)) v [ISUP](/mobilnisite/slovnik/isup/) nebo požadavek INVITE v SIP, aby extrahovala a přeposlala identitu volající linky.

Fungování CLIP zahrnuje několik klíčových komponent a signalizačních kroků. Při zahájení hovoru obsahuje zdrojové MSC nebo IMS uzel číslo volajícího ve signalizační zprávě pro sestavení hovoru. Tato informace, známá jako Calling Party Number ([CPN](/mobilnisite/slovnik/cpn/)) nebo formálněji jako Calling Line Identity ([CLI](/mobilnisite/slovnik/cli/)), je přenášena sítí prostřednictvím protokolů SS7, SIGTRAN nebo SIP. Obsluhující MSC nebo IMS Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) pro volanou stranu zkontroluje profil služby účastníka uložený v HLR nebo Home Subscriber Server (HSS), aby ověřil, zda je CLIP aktivní. Pokud je povoleno, síť přepošle CLI na terminál volané strany, typicky během fáze vyzvání, což umožní jeho zobrazení na obrazovce.

V rádiovém přístupu a interakci s terminálem, jakmile se MSC nebo IMS uzel rozhodne prezentovat CLI, odešle jej na mobilní stanici přes základnový stanovišťový systém. U hovorů v přepojování okruhů je toto často neseno v Facility Information Elements uvnitř zpráv řízení hovoru. U hovorů založených na IMS v novějších verzích je CLI přenášeno v hlavičce P-Asserted-Identity SIP zprávy INVITE nebo následných zpráv. Modem mobilní stanice a protokolový zásobník tuto informaci dekódují a předají uživatelskému rozhraní k zobrazení. CLIP také interaguje s dalšími službami, jako je Calling Line Identification Restriction (CLIR), kde volající může požadovat soukromí, což vede k rozhodnutí sítě, zda prezentaci potlačit na základě předplatného a regulatorních pravidel.

Role CLIP přesahuje pouhé zobrazení; je nedílnou součástí interakce služeb a síťové inteligence. Umožňuje nadstandardní služby, jako jsou seznamy zmeškaných hovorů, funkce zpětného volání a integrace s adresáři. V architektuře IMS je CLIP součástí Telephony Service for IMS (TAS) a využívá initial Filter Criteria (iFC) ke spuštění příslušné servisní logiky. Bezpečnostní aspekty zahrnují ověření pravosti CLI, aby se zabránilo podvržení, což je často řešeno pomocí signalizačních bezpečnostních mechanismů v core síti. Služba je definována napříč mnoha specifikacemi 3GPP, což zajišťuje interoperabilitu mezi různými síťovými elementy a generacemi, od GSM po 5G.

## K čemu slouží

CLIP byl vytvořen, aby řešil potřebu transparentnosti hovorů a uživatelské kontroly v telefonních sítích, čímž řeší problém anonymních nebo neočekávaných hovorů. Historicky, před jeho zavedením, neměla volaná strana žádný způsob, jak identifikovat volajícího před přijetím hovoru, což vedlo k neefektivitě, potenciálním bezpečnostním rizikům a zmeškání příležitostí pro správu hovorů. Služba vzešla z inovací v pevné telefonii a byla standardizována v 3GPP, aby přinesla tyto výhody do mobilních sítí, a obohatila tak základní hovorovou službu o inteligentní funkce.

Primární motivací pro CLIP je zlepšení uživatelského komfortu tím, že umožňuje třídění hovorů a účastníkům rozhodnout se, zda hovor přijmout na základě identity volajícího. To řeší praktické problémy, jako je vyhýbání se nechtěným hovorům, upřednostňování důležitých hovorů a usnadnění funkce zpětného volání. Také podporuje obchodní a tísňové služby poskytováním spolehlivé identifikace volajícího. Omezení předchozích přístupů, jako byla manuální asistence operátora nebo nedostatek standardizované signalizace, byla řešena integrací CLIP do digitální signalizační struktury sítí 3GPP, což zajišťuje automatizované, spolehlivé a konzistentní doručování napříč různými síťovými operátory a regiony.

CLIP navíc položil základy pro pokročilé telefonní služby a regulatorní požadavky, jako je lokalizace tísňového volajícího nebo opatření proti podvodům. Vytvořením standardizovaného mechanismu pro předávání informací o volající straně umožnil interoperabilitu v prostředí více dodavatelů a připravil cestu pro následná vylepšení, jako je rozšířený CLIP (např. s prezentací jména) a integrace s internetovými komunikačními službami v pozdějších verzích 3GPP.

## Klíčové vlastnosti

- Zobrazuje číslo volajícího volanému účastníkovi před přijetím hovoru
- Funguje jako doplňková služba v sítích s přepojováním okruhů a v IMS sítích
- Využívá signalizační protokoly jako ISUP, SIP a MAP pro přenos identity
- Interaguje s HLR/HSS pro ověření profilu služby účastníka
- Podporuje interakci služeb s CLIR pro správu soukromí
- Umožňuje nadstandardní funkce jako třídění hovorů a seznamy zmeškaných hovorů

## Související pojmy

- [CLIR – Calling Line Identification Restriction](/mobilnisite/slovnik/clir/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TR 22.949** (Rel-19) — Privacy Requirements Study for 3GPP Services
- **TR 22.976** (Rel-2) — Release 2000 Services Overview
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.226** (Rel-19) — Global Text Telephony (GTT) Stage 2
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TS 24.407** (Rel-8) — OIP and OIR Simulation Services Protocol
- **TS 24.607** (Rel-19) — OIP and OIR Supplementary Services Stage 3
- **TS 33.831** (Rel-12) — Study on Spoofed Call Detection & Prevention

---

📖 **Anglický originál a plná specifikace:** [CLIP na 3GPP Explorer](https://3gpp-explorer.com/glossary/clip/)
