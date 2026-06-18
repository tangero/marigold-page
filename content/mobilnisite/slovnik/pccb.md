---
slug: "pccb"
url: "/mobilnisite/slovnik/pccb/"
type: "slovnik"
title: "PCCB – Private Call Call-Back"
date: 2025-01-01
abbr: "PCCB"
fullName: "Private Call Call-Back"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pccb/"
summary: "PCCB je doplňková služba pro Mission Critical Push-To-Talk (MCPTT), která umožňuje uživateli vyžádat si zpětné volání od obsazeného nebo nedostupného uživatele v soukromém hovoru. Uloží žádost o zpětn"
---

PCCB je doplňková služba pro Mission Critical Push-To-Talk, která umožňuje uživateli vyžádat si a automaticky přijmout zpětné volání od obsazeného uživatele v soukromém hovoru, jakmile se obě strany stanou dostupné.

## Popis

Private Call Call-Back (PCCB) je standardizovaná doplňková služba v rámci 3GPP Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)), konkrétně definovaná pro Mission Critical Push-To-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)). Funguje v rámci vrstvy IP Multimedia Subsystem (IMS) sítě. Služba umožňuje uživateli MCPTT (volajícímu), který se pokusí navázat soukromý hovor (hovor jeden na jednoho) s jiným uživatelem (příjemcem), ale zjistí, že je obsazený, nedostupný, nebo neodpovídá, aktivovat žádost PCCB. Síť tuto žádost následně uloží ve stavu PCCB.

Architektonicky je logika služby PCCB umístěna na aplikačním serveru MCPTT ([AS](/mobilnisite/slovnik/as/)), což je IMS aplikační server rozšířený pro kritickou komunikaci. Když se sestavení soukromého hovoru nezdaří kvůli stavu příjemce, může iniciující MCPTT klient odeslat požadavek [SIP](/mobilnisite/slovnik/sip/) INVITE se specifickou indikací pro PCCB, nebo následný SIP požadavek jako MESSAGE. MCPTT AS, který funguje jako poskytovatel služby PCCB, žádost potvrdí a monitoruje stav dostupnosti cílového uživatele. Toto monitorování využívá informace o registraci a přítomnosti z IMS jádra. Jakmile MCPTT AS zjistí, že cílový uživatel je registrovaný a dostupný pro službu MCPTT (např. není v jiné MCPTT relaci a má pokrytí službou), automaticky iniciuje nové sestavení soukromého hovoru mezi oběma stranami, čímž vyhoví zpětnému volání.

Mezi klíčové zahrnuté komponenty patří MCPTT klient na uživatelském zařízení (UE), MCPTT AS hostující logiku služby PCCB a podkladové IMS jádro poskytující schopnosti registrace, řízení relací a přítomnosti. Služba funguje tak, že udržuje záznam PCCB obsahující identity volajícího a příjemce, časové razítko žádosti a její stav (např. čekající, zpracovává se). MCPTT AS spravuje životní cyklus tohoto záznamu, včetně časovačů expirace, aby zabránil neomezeně čekajícím stavům. Jeho úlohou je zvýšit spolehlivost a úspěšnost kritické komunikace jeden na jednoho automatizací logiky opakování, čímž zajišťuje, že důležité hovory nejsou zmeškané kvůli dočasné nedostupnosti.

## K čemu slouží

PCCB byla vytvořena, aby vyřešila kritickou provozní mezeru v komunikaci push-to-talk pro uživatele veřejné bezpečnosti a pracovníky v misích kritických pro chod. Ve vysoce rizikových prostředích, jako je zásah při mimořádné události, je nezbytné, aby pokusy o komunikaci uspěly. Tradiční mobilní hovory nebo základní služby [PTT](/mobilnisite/slovnik/ptt/) při nedostupnosti příjemce pouze vrátí obsazený tón nebo přepojí do hlasové schránky, což je nepřijatelné, když je třeba doručit naléhavé pokyny nebo informace o stavu. PCCB poskytuje mechanismus garantovaného doručení pokusů o soukromý hovor.

Problém, který řeší, je neefektivita a potenciální selhání ručního opakování. Bez PCCB musí uživatel, který narazí na obsazeného kolegu, opakovaně zkoušet volat, což plýtvá časem a pozorností během kritických incidentů. PCCB tento proces automatizuje a přesouvá úlohu opakování na síť. To bylo motivováno požadavky definovanými uživateli profesionální mobilní rádiové komunikace a standardizačními orgány, jako je [TCCA](/mobilnisite/slovnik/tcca/), které byly integrovány do specifikací [MCPTT](/mobilnisite/slovnik/mcptt/) 3GPP počínaje Release 13. Řeší omezení předchozích PTT systémů, kterým často chyběly inteligentní, síťově spravované doplňkové služby.

Navíc PCCB zvyšuje efektivitu týmové koordinace. Tím, že zajišťuje zařazení žádosti o zpětné volání do fronty a její automatické provedení, umožňuje volajícímu pokračovat v jiných úkolech s jistotou, že spojení bude navázáno. To je v souladu s širším posláním 3GPP poskytovat na úrovni operátora kvalitní, funkcemi bohatou kritickou komunikaci přes sítě LTE a 5G, čímž nahrazuje nebo doplňuje starší systémy jako [TETRA](/mobilnisite/slovnik/tetra/) nebo P25 flexibilnějšími a IP-based službami.

## Klíčové vlastnosti

- Automatická iniciace zpětného volání pro neúspěšné pokusy o soukromý MCPTT hovor
- Síťové ukládání a správa žádostí o zpětné volání
- Integrace s IMS registrací a přítomností pro monitorování dostupnosti
- Podpora konfigurovatelných časovačů expirace pro čekající žádosti o zpětné volání
- Upozornění uživatelů na aktivaci a dokončení PCCB
- Zajišťuje spolehlivou komunikaci jeden na jednoho ve scénářích kritických pro misi

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [PCCB na 3GPP Explorer](https://3gpp-explorer.com/glossary/pccb/)
