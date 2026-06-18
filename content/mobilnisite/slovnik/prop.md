---
slug: "prop"
url: "/mobilnisite/slovnik/prop/"
type: "slovnik"
title: "PROP – Proprietary Field"
date: 2025-01-01
abbr: "PROP"
fullName: "Proprietary Field"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/prop/"
summary: "Vyhrazené pole uvnitř zpráv protokolů 3GPP, které umožňuje dodavatelům a operátorům implementovat proprietární, nestandardizovaná rozšíření. Umožňuje přizpůsobení a diferenciaci při zachování celkové"
---

PROP je vyhrazené pole uvnitř zpráv protokolů 3GPP, které umožňuje dodavatelům a operátorům implementovat proprietární, nestandardizovaná rozšíření pro přizpůsobení.

## Popis

Proprietární pole (PROP) je standardizovaný mechanismus ve specifikacích 3GPP, primárně definovaný v TS 33.204, který vyčleňuje specifický, rezervovaný prostor uvnitř přenosových jednotek protokolů ([PDU](/mobilnisite/slovnik/pdu/)) pro data specifická pro dodavatele nebo operátora. Toto pole je úmyslně ponecháno nedefinované standardizačním orgánem 3GPP, což umožňuje výrobcům zařízení a síťovým operátorům vkládat vlastní informace, funkce nebo optimalizace, které nejsou součástí univerzální specifikace. Jeho přítomnost je v protokolovém zásobníku akceptována, což zajišťuje, že standardizované síťové elementy mohou tuto část správně zpracovat a ignorovat, aniž by došlo k poruše interoperability, čímž je zachována integrita komunikace end-to-end.

Z architektonického hlediska je pole PROP typicky vnořeno do zpráv signalizace vyšší vrstvy nebo do uživatelské roviny, jako jsou například zprávy Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) nebo specifických aplikačních protokolů. Jeho přesná poloha a délka jsou definovány v příslušných protokolových specifikacích, aby se předešlo nejednoznačnostem. Když síťový prvek přijme zprávu obsahující pole PROP, zpracuje standardizované části zprávy podle pravidel 3GPP. Pokud je prvek od stejného dodavatele nebo operátora, který pole PROP naplnil, může proprietární obsah dekódovat a podle něj jednat; v opačném případě jej jednoduše přeskočí. Tento návrh vyžaduje, aby proprietární implementace využívající pole PROP byly zpětně kompatibilní a nenarušovaly základní, standardizovanou funkčnost sítě.

Role pole PROP je klíčová pro podporu inovací a konkurence mezi dodavateli ve standardizovaném ekosystému. Umožňuje nasazení jedinečných funkcí, jako jsou specializované bezpečnostní algoritmy, parametry optimalizace sítě nebo experimentální funkcionality, aniž by bylo nutné pro každé drobné vylepšení absolvovat zdlouhavý standardizační proces. Jeho použití je však inherentně neinteroperabilní, což znamená, že jeho výhody jsou typicky omezeny na zařízení jednoho dodavatele nebo na síť konkrétního operátora. Z pohledu provozu sítě musí být pole PROP pečlivě spravováno, aby se předešlo konfliktům s budoucími standardizovanými rozšířeními, která by mohla obsadit stejný prostor ve zprávě, a aby se zajistilo, že proprietární implementace neohrozí neúmyslně bezpečnost nebo stabilitu sítě.

## K čemu slouží

Pole PROP bylo zavedeno k řešení zásadního napětí v telekomunikační standardizaci: potřeby globálně interoperabilních protokolů oproti snaze jednotlivých dodavatelů a operátorů diferencovat své produkty a služby. Před jeho formalizací mohli dodavatelé implementovat proprietární rozšíření ad hoc, což mohlo potenciálně narušit formát zpráv a způsobit problémy s interoperabilitou se zařízeními od jiných dodavatelů. Pole PROP poskytuje vyhrazený 'sandbox' uvnitř protokolu, který umožňuje inovace a přizpůsobení bez porušení standardizovaného rámce.

K jeho vytvoření vedla komerční realita, že konkurenční diferenciace je na telekomunikačním trhu nezbytná. Operátoři mohou vyžadovat specifické funkce přizpůsobené své jedinečné topologii sítě, regulatornímu prostředí nebo nabídce služeb. Standardizace každé možné funkce by byla nepraktická a pomalá. Pole PROP tedy slouží jako pojistný ventil, umožňující rychlé nasazení proprietárních řešení, zatímco se standardizační orgán soustředí na univerzální požadavky. Řeší omezení čistě statických specifikací tím, že umožňuje vývoj a specializaci.

Historicky, jak se sítě vyvíjely z 3G přes 4G na 5G, složitost služeb vzrostla, což dále zvýšilo potřebu takových flexibilních polí. Pole PROP, specifikované v bezpečnostním kontextu TS 33.204, také podtrhuje jeho význam pro umožnění proprietárních bezpečnostních vylepšení, která mohou být klíčová pro splnění specifických národních regulací nebo pro implementaci špičkové, nestandardizované kryptografické ochrany předtím, než je široce přijata standardizační komunitou.

## Klíčové vlastnosti

- Zapouzdření dat specifických pro dodavatele
- Zachovává shodu s protokolem a interoperabilitu
- Definovaná pozice uvnitř zpráv protokolu pro prevenci chyb při zpracování
- Umožňuje rychlé nasazení nestandardizovaných funkcí
- Podporuje optimalizace sítě specifické pro operátora
- Umožňuje implementaci proprietárních bezpečnostních algoritmů

## Související pojmy

- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TS 33.204** (Rel-19) — TCAP Security (TCAPsec) Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [PROP na 3GPP Explorer](https://3gpp-explorer.com/glossary/prop/)
