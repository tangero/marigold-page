---
slug: "afe"
url: "/mobilnisite/slovnik/afe/"
type: "slovnik"
title: "AFE – Advanced Front-end"
date: 2025-01-01
abbr: "AFE"
fullName: "Advanced Front-end"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/afe/"
summary: "AFE je sofistikovaná RF front-endová komponenta v uživatelském zařízení 3GPP, zodpovědná za úpravu signálu mezi anténou a základnovým procesorem. Provádí kritické analogové zpracování, jako je filtrac"
---

AFE je pokročilá RF front-endová komponenta v uživatelském zařízení, která provádí kritické analogové úpravy signálu, jako je filtrace a zesílení, mezi anténou a základnovým procesorem, aby podporovala široká pásma a agregaci nosných.

## Popis

Advanced Front-end (AFE) je kritický hardwarový subsystém v uživatelském zařízení (UE) 3GPP, umístěný mezi anténním rozhraním a digitálním základnovým procesorem. Slouží jako primární řetězec analogového zpracování signálu, který upravuje přijímané [RF](/mobilnisite/slovnik/rf/) signály před digitální konverzí a připravuje vysílané signály k vyzařování. Architektura AFE typicky zahrnuje šumově nízké zesilovače ([LNA](/mobilnisite/slovnik/lna/)) pro zesílení signálu v přijímací cestě, výkonové zesilovače ([PA](/mobilnisite/slovnik/pa/)) pro zesílení výkonu ve vysílací cestě, měniče pro převod frekvence mezi RF a mezifrekvencemi a sofistikované filtry pro výběr pásma a potlačení rušení. Tyto komponenty spolupracují na zachování integrity signálu napříč širokými frekvenčními rozsahy a komplexními modulačními schématy používanými v moderních mobilních standardech.

Během provozu přijímací cesta AFE zachytí slabé RF signály z antény, zesílí je s minimálním přidaným šumem pomocí LNA, odfiltruje mimopásmové rušení pomocí povrchových akustických vln (SAW) nebo objemových akustických vln (BAW) filtrů a převede signály na mezifrekvence vhodné pro analogově-digitální převod. Vysílací cesta provádí opačný proces: převádí základnové signály na RF frekvence, zesiluje je na příslušné výkonové úrovně pomocí PA s pečlivou kontrolou linearity a aplikuje filtraci pro splnění požadavků spektrální masky před vysíláním. Moderní AFE začleňují pokročilé techniky, jako je sledování obálky pro zlepšení účinnosti PA a podpora agregace nosných pro zvládnutí simultánního vysílání na více kmitočtových pásmech.

Role AFE přesahuje základní úpravu signálu a zahrnuje kritické funkce výkonu sítě. Implementuje správu dynamického rozsahu pro zvládnutí proměnlivé síly signálu od okraje buňky po střed buňky, podporuje konfigurace [MIMO](/mobilnisite/slovnik/mimo/) prostřednictvím paralelních RF řetězců a zajišťuje izolaci mezi vysílací a přijímací cestou, aby zabránila vlastnímu rušení. Subsystém také zahrnuje obvody pro správu napájení, které optimalizují spotřebu baterie na základě požadavků na vysílací výkon a podmínek signálu. Ve scénářích agregace nosných musí AFE zvládat simultánní signály napříč nesousedními kmitočtovými pásmy s minimální intermodulační distorzí, což vyžaduje sofistikované filtrační architektury a lineární zesilovací stupně.

Specifikace 3GPP definují požadavky na výkon komponent AFE, aby zajistily interoperabilitu a výkon sítě. Mezi ně patří parametry jako šumové číslo (typicky 3–6 dB pro přijímací řetězce), poměr úniku do sousedního kanálu ([ACLR](/mobilnisite/slovnik/aclr/)) pro vysílací řetězce (lepší než -45 dBc pro LTE) a příspěvek k velikosti chybového vektoru ([EVM](/mobilnisite/slovnik/evm/)). Návrh AFE přímo ovlivňuje klíčové metriky UE včetně citlivosti (minimální přijatelný výkon signálu), maximálního výstupního výkonu a výdrže baterie. Jak se mobilní technologie vyvíjely od 3G přes 4G až po 5G, složitost AFE dramaticky vzrostla, aby podporovala širší pásma (až 100 MHz v 5G NR), vyšší frekvenční rozsahy (včetně milimetrových vln) a komplexnější modulační schémata (až 256-QAM v LTE a 1024-QAM v 5G).

## K čemu slouží

Advanced Front-end byl vyvinut, aby řešil rostoucí složitost požadavků na [RF](/mobilnisite/slovnik/rf/) zpracování signálu v více režimových a více pásmových mobilních zařízeních. Jak se standardy 3GPP vyvíjely od verze Rel-8 dále, uživatelská zařízení potřebovala podporovat rostoucí počet kmitočtových pásem, širší kanálová pásma a pokročilé funkce, jako je agregace nosných. Tradiční návrhy RF front-endu těmto požadavkům čelily kvůli omezením ve selektivitě filtrů, linearitě zesilovačů a energetické účinnosti. Koncept AFE vznikl jako integrované řešení, které dokáže tyto výzvy zvládnout při zachování kompaktního provedení vhodného pro smartphony a další mobilní zařízení.

Předchozí implementace front-endu používaly diskrétní komponenty optimalizované pro konkrétní pásma nebo režimy, což vyžadovalo více paralelních řetězců pro globální roamingové schopnosti. Tento přístup vedl k velkým nárokům na plochu desky s plošnými spoji, vysoké spotřebě energie a výrobní složitosti. Architektura AFE konsolidovala tyto funkce do více integrovaných řešení se sdílenými komponentami tam, kde to bylo možné, při zachování výkonové izolace potřebné pro simultánní více pásmový provoz. Řešila kritické problémy, jako je potlačení harmonických pro agregaci nosných, tepelné řízení výkonových zesilovačů a potlačení rušení v přeplněném RF prostředí.

Vytvoření technologie AFE bylo motivováno komerční potřebou zařízení, která by mohla fungovat globálně napříč desítkami kmitočtových pásem a zároveň podporovat zpětnou kompatibilitu se sítěmi 2G, 3G a 4G. Síťoví operátoři požadovali zařízení schopná využívat agregaci nosných pro vyšší datové rychlosti, což vyžadovalo front-endy schopné zpracovávat více simultánních signálů s minimálními intermodulačními produkty. Pokročilé filtrační, spínací a zesilovací schopnosti AFE tyto funkce umožnily, přičemž celkovou složitost systému dokonce snížily díky lepší integraci. Tento technologický pokrok byl zásadní pro revoluci smartphonů, protože umožnil výrobcům vyrábět globálně kompatibilní zařízení v kompaktním provedení s přijatelnou výdrží baterie.

## Klíčové vlastnosti

- Podpora více pásem prostřednictvím laditelných filtrů a přepínačů
- Schopnost agregace nosných s vysoce lineárními komponentami
- Integrované výkonové zesilovače se sledováním obálky pro vyšší účinnost
- Návrhy šumově nízkých zesilovačů se šumovým číslem pod 4 dB
- Pokročilá filtrace využívající technologii BAW/SAW pro potlačení rušení
- Podpora konfigurací MIMO s více paralelními RF řetězci

## Definující specifikace

- **TS 26.177** (Rel-19) — DSR Extended Advanced Front-end Test Sequences
- **TS 26.243** (Rel-19) — DSR Extended Advanced Front-end C Code
- **TR 26.943** (Rel-19) — SES Codec Selection Report

---

📖 **Anglický originál a plná specifikace:** [AFE na 3GPP Explorer](https://3gpp-explorer.com/glossary/afe/)
