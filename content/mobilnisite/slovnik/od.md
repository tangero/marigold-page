---
slug: "od"
url: "/mobilnisite/slovnik/od/"
type: "slovnik"
title: "OD – Operator Determined"
date: 2025-01-01
abbr: "OD"
fullName: "Operator Determined"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/od/"
summary: "Označení ve specifikacích 3GPP, které označuje funkci nebo parametr, jehož implementace je ponechána na uvážení operátora. Poskytuje flexibilitu, která operátorům umožňuje přizpůsobit chování sítě na"
---

OD je označení ve specifikacích 3GPP pro funkci nebo parametr, jehož implementace je ponechána na uvážení operátora, což poskytuje flexibilitu při nasazení.

## Popis

Operator Determined (OD) je normativní kvalifikátor používaný v technických specifikacích (TS) a technických zprávách (TR) 3GPP. Když je funkce, parametr, procedura nebo schopnost označena jako 'OD', znamená to, že standard 3GPP definuje její chování a rozhraní, ale výslovně uvádí, že rozhodnutí o tom, zda a jak bude implementována v živé síti, přísluší jednotlivému mobilnímu síťovému operátorovi ([MNO](/mobilnisite/slovnik/mno/)). Specifikace poskytuje technický rámec, ale volba nasadit, nakonfigurovat a aktivovat funkci je specifická pro operátora. To je často dokumentováno ve specifikacích jako TS 21.905 (slovníček) a TS 28.062 (aspekty řízení).

V praxi se prvky OD objevují v mnoha kontextech. Například ve specifikacích pro správu sítě (např. pro rozhraní Itf-N) mohou být některá měření výkonu nebo konfigurační parametry OD, což znamená, že se operátorův Operations Support System ([OSS](/mobilnisite/slovnik/oss/)) může rozhodnout je sbírat nebo nastavovat na základě interních politik. Ve specifikacích pro rádiový přístupovou síť (RAN) může být práh určitého parametru pro předávání hovoru nebo příznak aktivace funkce OD, což operátorům umožňuje optimalizovat síť pro jejich jedinečné rádiové prostředí (hustá městská zástavba vs. venkov) nebo vzorce provozu. Ve specifikacích pro jádro sítě může být podpora určitých doplňkových služeb nebo funkcí pro spolupráci OD.

Architektonická role OD spočívá v nalezení rovnováhy mezi standardizací a flexibilitou. Standardizace zajišťuje interoperabilitu mezi zařízeními od různých dodavatelů (např. že UE od dodavatele A funguje v síti používající RAN dodavatele B). Označení OD vnáší flexibilitu do vrstvy nasazení a uznává, že přístup 'jedna velikost pro všechny' není praktický pro globální operátory s různorodými potřebami. Při implementaci položky OD operátor definuje její hodnotu nebo politiku ve svých dokumentech návrhu sítě, které pak vedou konfiguraci síťových prvků ([NE](/mobilnisite/slovnik/ne/)), jako jsou základnové stanice, [MME](/mobilnisite/slovnik/mme/) nebo [SCP](/mobilnisite/slovnik/scp/). Zařízení od dodavatelů musí podporovat standardizované chování, ale budou nakonfigurována podle rozhodnutí operátora ohledně OD.

## K čemu slouží

Koncept Operator Determined existuje k vyřešení napětí mezi potřebou přísných globálních standardů pro interoperabilitu a praktickou nutností lokální optimalizace a diferenciace sítě. Standardy 3GPP musí být dostatečně přesné, aby zaručily, že zařízení a sítě po celém světě spolu fungují. Pokud by však každý jednotlivý parametr a funkce byly povinné, potlačilo by to inovace, zabránilo optimalizaci nákladů a učinilo sítě nepružnými. Operátoři v různých zemích čelí různým přidělením spektra, regulatorním požadavkům, tržní konkurenci a hustotě účastníků.

OD poskytuje v rámci standardizačního procesu nezbytný 'únikový ventil'. Umožňuje specifikaci být kompletní pro testování interoperability a zároveň dává operátorům komerční a technickou svobodu rozhodnout, co je nejlepší pro jejich konkrétní nasazení. Například operátor zaměřený na nízkonákladové IoT může deaktivovat OD funkci pro vylepšené mobilní širokopásmoví, aby zjednodušil své jádro sítě. Historicky, jak se sítě vyvíjely od 2G přes 3G a dále, složitost funkcí exponenciálně rostla. Mechanismus OD se stal klíčovým pro správu této složitosti, což umožnilo standardu zahrnout širokou škálu pokročilých schopností, aniž by nutil každého operátora implementovat je všechny od prvního dne. Řeší tak omezení příliš rigidních specifikací, které se nedokázaly přizpůsobit různým obchodním cílům a tempu technologického vývoje.

## Klíčové vlastnosti

- Normativní kvalifikátor ve specifikacích 3GPP označující, že implementace je na uvážení operátora.
- Poskytuje flexibilitu nasazení při zachování standardizovaných rozhraní a chování.
- Aplikuje se na funkce, parametry, prahové hodnoty a indikátory podpory.
- Rozhodnutí jsou dokumentována v dokumentech návrhu sítě a pravidlech politiky operátora.
- Kritické pro interoperabilitu zařízení od různých dodavatelů navzdory proměnným nasazením.
- Umožňuje diferenciaci operátorů a optimalizaci pro konkrétní trh.

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description

---

📖 **Anglický originál a plná specifikace:** [OD na 3GPP Explorer](https://3gpp-explorer.com/glossary/od/)
