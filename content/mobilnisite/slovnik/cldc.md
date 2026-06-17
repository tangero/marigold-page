---
slug: "cldc"
url: "/mobilnisite/slovnik/cldc/"
type: "slovnik"
title: "CLDC – Connected Limited Device Configuration"
date: 2025-01-01
abbr: "CLDC"
fullName: "Connected Limited Device Configuration"
category: "IoT"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/cldc/"
summary: "Standardizovaný rámec konfigurace zařízení pro zařízení IoT s omezenými prostředky v sítích 3GPP. Definuje minimální schopnosti a požadavky pro zařízení s omezenou pamětí, výpočetním výkonem a životno"
---

CLDC je standardizovaný 3GPP rámec pro zařízení IoT s omezenými prostředky, který definuje minimální schopnosti pro zajištění interoperability a optimalizaci z hlediska nákladů a energetické účinnosti.

## Popis

Connected Limited Device Configuration (CLDC) je komplexní rámec v rámci specifikací 3GPP, který stanovuje standardizované konfigurace pro zařízení IoT s omezenými prostředky. Na rozdíl od tradičních mobilních zařízení pracují zařízení CLDC pod přísnými omezeními v paměti (RAM i ROM), výpočetní kapacitě a dostupnosti energie. Rámec definuje povinné a volitelné schopnosti napříč více vrstvami protokolového zásobníku, což zajišťuje, že tato zařízení se mohou připojit k celulárním sítím při zachování minimální složitosti a nákladů.

Z architektonického hlediska CLDC zahrnuje specifikace pro adaptace fyzické vrstvy, zjednodušené procedury řízení rádiových prostředků a optimalizované signalizační protokoly. Definuje, jak tato zařízení komunikují se sítí během fází připojení, mobility a přenosu dat. Mezi klíčové komponenty patří mechanismy úspory energie, jako je rozšířené nespojité příjímání (eDRX) a režim úspory energie (PSM), zjednodušené autentizační procedury a podpora optimalizací pro přenos malých objemů dat. Konfigurace také řeší požadavky na správu paměti, specifikuje minimální velikosti vyrovnávacích pamětí a výpočetní schopnosti potřebné pro základní celulární operace.

V síťovém provozu zařízení CLDC implementují zjednodušené verze standardních protokolů za účelem snížení signalizační režie a výpočetních požadavků. To zahrnuje zjednodušené stavy [RRC](/mobilnisite/slovnik/rrc/), redukované procedury správy mobility a optimalizované mechanismy pagingu. Rámec zajišťuje, že tato zařízení mohou udržovat síťovou konektivitu při spotřebě minimální energie, což často umožňuje životnost baterie v řádu několika let. Konfigurace CLDC jsou navrženy tak, aby fungovaly s rádiovými technologiemi LTE-M i NB-IoT, což poskytuje flexibilitu pro různé případy užití IoT s různými požadavky na přenosovou rychlost, latenci a pokrytí.

Role CLDC v síťovém ekosystému je klíčová pro umožnění masivního nasazení IoT. Standardizací minimálních schopností zařízení s omezenými prostředky umožňuje síťovým operátorům efektivně spravovat různorodé populace zařízení IoT při zachování výkonu sítě. Rámec také usnadňuje certifikaci zařízení a testování interoperability, protože výrobci mohou navrhovat produkty podle dobře definovaných konfiguračních profilů. Tato standardizace snižuje fragmentaci na trhu IoT a umožňuje dosáhnout úspor z rozsahu ve výrobě zařízení.

## K čemu slouží

CLDC byl vytvořen, aby řešil základní výzvu připojení masivního počtu zařízení s omezenými prostředky k celulárním sítím. Před jeho zavedením byly standardy 3GPP primárně navrženy pro chytré telefony a další výkonná zařízení s dostatečným výpočetním výkonem, pamětí a energetickými zdroji. Tyto tradiční specifikace se nehodily pro zařízení IoT, která potřebovala pracovat roky na bateriový pohon s minimální hardwarovou složitostí. Vysoká cena a spotřeba energie standardních celulárních modemů bránila širokému přijetí celulární technologie pro nízkonákladové aplikace IoT.

Historický kontext pro vývoj CLDC vznikl během 3GPP Release 10, kdy průmysl rozpoznal rostoucí potenciál komunikace mezi stroji (M2M). Raná zařízení M2M používala modifikované verze stávajících celulárních standardů, což vedlo k problémům s interoperabilitou a suboptimálnímu výkonu. CLDC poskytl standardizovaný přístup ke konfiguraci zařízení, který vyvážil funkčnost s omezeními, a umožnil tak nákladově efektivní celulární řešení IoT. Vyřešil problém, jak zachovat zpětnou kompatibilitu se stávajícími sítěmi a zároveň akomodovat zařízení s řádově menšími schopnostmi než tradiční uživatelská zařízení (UE).

Definováním jasných konfiguračních profilů CLDC řešil omezení předchozích přístupů, kdy se schopnosti zařízení výrazně lišily, což ztěžovalo optimalizaci sítě. Umožnil síťovým operátorům implementovat specifické optimalizace pro zařízení s omezenými prostředky, aniž by to ovlivnilo služby pro tradiční chytré telefony. Rámec také usnadnil vývoj specializovaných rádiových technologií pro IoT, jako jsou LTE-M a NB-IoT, tím, že poskytl standardizovanou výchozí konfiguraci zařízení, která mohla být optimalizována pro různé případy užití při zachování základních principů celulární konektivity.

## Klíčové vlastnosti

- Standardizované minimální schopnosti pro paměť a zpracování
- Optimalizované mechanismy úspory energie včetně eDRX a PSM
- Zjednodušená signalizace a snížená režie protokolů
- Podpora pro rádiové technologie LTE-M i NB-IoT
- Zpětná kompatibilita se stávajícími celulárními sítěmi
- Vylepšené pokrytí pro hluboké vnitřní a venkovské nasazení

## Definující specifikace

- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [CLDC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cldc/)
