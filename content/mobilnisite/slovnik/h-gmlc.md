---
slug: "h-gmlc"
url: "/mobilnisite/slovnik/h-gmlc/"
type: "slovnik"
title: "H-GMLC – Home-Gateway Mobile Location Centre"
date: 2025-01-01
abbr: "H-GMLC"
fullName: "Home-Gateway Mobile Location Centre"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/h-gmlc/"
summary: "Home-Gateway Mobile Location Centre (H-GMLC) je entita jádrové sítě, která v domovské síti uživatele slouží jako primární brána pro požadavky na lokalizační služby. Přijímá lokalizační požadavky od ex"
---

H-GMLC je brána jádrové sítě v domovské síti uživatele, která ověřuje a předává požadavky na lokalizační služby od externích klientů za účelem získání polohy uživatele pro služby, jako jsou tísňová volání.

## Popis

Home-Gateway Mobile Location Centre (H-GMLC) je klíčový uzel v architektuře lokalizačních služeb ([LCS](/mobilnisite/slovnik/lcs/)) podle 3GPP, standardizovaný napříč několika vydáními počínaje Rel-8. Nachází se v domovské veřejné pozemní mobilní síti ([HPLMN](/mobilnisite/slovnik/hplmn/)) účastníka a slouží jako první kontaktní bod pro jakoukoli externí entitu (známou jako LCS Client) žádající o geografickou polohu mobilního účastníka. Mezi primární funkce H-GMLC patří autentizace žadatele, ověření pravidel ochrany soukromí a správa relace. Po přijetí lokalizačního požadavku ověří přihlašovací údaje LCS Clienta a zkontroluje nastavení ochrany soukromí cílového účastníka uložená v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), aby zajistila, že je požadavek povolen. Pokud je autorizován, H-GMLC určí aktuální síť, ve které se cílový uživatel nachází. Pokud je uživatel v domovské síti, H-GMLC předá požadavek přímo místnímu Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) nebo Serving Mobile Location Centre (SMLC). Pokud uživatel roamuje, H-GMLC směruje požadavek na příslušný Visited-GMLC (V-GMLC) v navštívené veřejné pozemní mobilní síti (VPLMN). H-GMLC komunikuje s HSS přes rozhraní Lh, aby získala směrovací informace a profily ochrany soukromí účastníka. S ostatními GMLC (V-GMLC nebo místním GMLC) komunikuje pomocí rozhraní Lr/Lg. H-GMLC také zajišťuje formátování a zabezpečené doručení výsledného odhadu polohy (např. zeměpisná šířka, délka, přesnost) zpět žádajícímu LCS Clientovi. Její architektura je navržena tak, aby centralizovala řízení a správu ochrany soukromí v domovské síti, což zajišťuje konzistentní aplikaci pravidel bez ohledu na fyzickou polohu účastníka.

## K čemu slouží

H-GMLC byla zavedena za účelem poskytnutí standardizované, bezpečné a na ochranu soukromí zaměřené brány pro získání polohy mobilních účastníků, což se stalo stále důležitějším s nástupem lokalizačních služeb a regulačních požadavků, jako je Enhanced 911 (E911) v USA a eCall v Evropě. Před její standardizací byly metody lokalizace uživatelů často proprietární a postrádaly robustní kontrolu ochrany soukromí, zejména v roamingu. H-GMLC řeší problém, jak může externí aplikace nebo služba spolehlivě a bezpečně požádat o polohu uživatele při respektování jeho preferencí ochrany soukromí a bezpečnostních politik operátora. Centralizuje autorizační funkci v domovské síti, kde jsou uložena smluvní ujednání a pravidla ochrany soukromí účastníka. To operátorům umožňuje udržovat kontrolu nad zveřejňováním lokalizačních údajů a nabízet [LCS](/mobilnisite/slovnik/lcs/) jako zpoplatněnou službu. Její vytvoření umožnilo širokou škálu aplikací, od tísňových služeb (kde síť musí volajícího automaticky lokalizovat) až po komerční služby, jako je sledování vozového parku, lokalizační reklama nebo aplikace pro vyhledání přátel, a to díky poskytnutí dobře definovaného, interoperabilního rozhraní mezi mobilní sítí a externími poskytovateli služeb.

## Klíčové vlastnosti

- Primární vstupní bod v HPLMN pro externí požadavky na lokalizační služby (LCS)
- Autentizace a autorizace klientů lokalizačních služeb (žadatelů)
- Ověření kontroly ochrany soukromí vůči profilům účastníků v HSS
- Směrování lokalizačních požadavků do správné sítě (domovské nebo navštívené)
- Správa relace a koordinace procedur pro získání polohy
- Zabezpečené doručení odhadů polohy autorizovaným žadatelům

## Související pojmy

- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)

## Definující specifikace

- **TR 23.730** (Rel-14) — Study on extended CIoT architecture
- **TS 29.173** (Rel-19) — Diameter-based SLh Interface for LCS
- **TS 32.271** (Rel-19) — 3GPP LCS Charging Management Spec
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)

---

📖 **Anglický originál a plná specifikace:** [H-GMLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/h-gmlc/)
