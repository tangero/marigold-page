---
slug: "ml-mc"
url: "/mobilnisite/slovnik/ml-mc/"
type: "slovnik"
title: "ML/MC – Multilink-Multiclass PPP"
date: 2025-01-01
abbr: "ML/MC"
fullName: "Multilink-Multiclass PPP"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ml-mc/"
summary: "Rozšíření protokolu Point-to-Point Protocol (PPP), které umožňuje svazování více fyzických spojů do jediného logického spoje a podporuje více tříd provozu. Zvyšuje datovou propustnost a poskytuje dife"
---

ML/MC je rozšíření PPP, které sdružuje více fyzických spojů do jednoho logického spoje a podporuje více tříd provozu za účelem zvýšení propustnosti a poskytnutí diferencované QoS přes rozhraní Iub a Iur sítě UTRAN.

## Popis

[ML](/mobilnisite/slovnik/ml/)/[MC](/mobilnisite/slovnik/mc/), neboli Multilink-Multiclass PPP, je protokol definovaný v 3GPP pro rozhraní Iub a Iur v architektuře UTRAN. Funguje jako vylepšení standardního protokolu Point-to-Point Protocol (PPP), konkrétně navržené pro splnění náročných požadavků na šířku pásma a kvalitu služeb (QoS) v sítích 3G a novějších. Protokol funguje tak, že agreguje více fyzických přenosových spojů, jako jsou linky E1 nebo T1, do jediného logického datového kanálu. Tato agregace je řízena mechanismem multilink protokolu, který fragmentuje, sekvencuje a znovu sestavuje pakety napříč dostupnými spoji, čímž zvyšuje celkovou dostupnou šířku pásma a poskytuje vyrovnávání zátěže. Současně aspekt multiclass zavádí schopnost klasifikovat a upřednostňovat různé typy provozu (např. signalizaci, data uživatelské roviny, provoz O&M) na samostatné virtuální spoje neboli třídy v rámci tohoto agregovaného spoje. Toho je dosaženo rozšířením formátu PPP rámce o hlavičku Multiclass Protocol Data Unit (MC-PDU), která nese identifikační informace třídy.

Architektonicky je ML/MC implementován ve vrstvě transportní sítě (TNL) rozhraní Iub a Iur, nachází se nad fyzickou vrstvou a pod adaptačními vrstvami [ATM](/mobilnisite/slovnik/atm/) nebo IP podle příslušných specifikací. Mezi klíčové komponenty patří funkce svazování Multilink PPP (ML-PPP) a mechanismy rámcování a front multiclass (MC). Node B (pro Iub) i RNC (pro Iub a Iur) musí tento protokol podporovat, aby bylo možné agregovaný spoj navázat a udržovat. Protokol funguje tak, že během fáze navazování spoje vyjednává schopnosti pomocí Link Control Protocol ([LCP](/mobilnisite/slovnik/lcp/)) a specifického Multiclass Network Control Protocol (MC-NCP). Po navázání jsou datové pakety z vyšších vrstev klasifikovány, zapouzdřeny s hlavičkou MC-PDU označující třídu provozu a poté předány multilink komponentě. Multilink komponenta je zodpovědná za fragmentaci paketů (je-li nutná), přiřazení sekvenčních čísel a distribuci fragmentů napříč členskými spoji svazku pro přenos.

Její role v síti je klíčová pro efektivní využití přenosové sítě (backhaul) v UTRAN. Sdružením více nízkorychlostních TDM okruhů mohli operátoři vytvořit vyšší šířku pásma nákladově efektivně, aniž by museli okamžitě upgradovat na dražší vysokorychlostní spoje. Funkce multiclass zajišťuje, že na zpoždění citlivá signalizace řídicí roviny dostane vyšší prioritu než datový provoz s běžným doručením (best-effort), což je zásadní pro udržení stability hovorů a výkonu při předávání spojení. Protokol poskytuje standardizovaný, spolehlivý transportní mechanismus, který podporuje přísné požadavky na zpoždění, chvění a ztrátovost služeb UMTS, a tvoří tak páteř pro přenos provozu Frame Protocol ([FP](/mobilnisite/slovnik/fp/)) mezi síťovými prvky. Jeho návrh umožňuje odolnost; pokud jeden fyzický spoj ve svazku selže, provoz může být přerozdělen mezi zbývající spoje, i když za snížené celkové šířky pásma.

## K čemu slouží

[ML/MC-PPP](/mobilnisite/slovnik/ml-mc-ppp/) bylo vytvořeno, aby řešilo specifické transportní výzvy v raných sítích 3G UMTS, zejména pro rozhraní Iub spojující Node B s Radio Network Controller (RNC). Před 3G často přenosová připojení (backhaul) používala jednotlivé linky E1/T1 se základním PPP nebo adaptací [ATM](/mobilnisite/slovnik/atm/). Zvýšené datové rychlosti a rozmanité požadavky služeb (hlas, video, data) UMTS však vyžadovaly více šířky pásma a sofistikované zpracování Quality of Service (QoS) od transportní sítě. Nasazení nových pronajatých linek s vysokou kapacitou (jako STM-1) bylo pro mnoho lokalit buněk finančně neúnosné. ML/[MC](/mobilnisite/slovnik/mc/) poskytlo ekonomické řešení tím, že umožnilo operátorům kombinovat více stávajících nebo nových nízkonákladových linek E1 a agregovat jejich kapacitu, aby uspokojili rostoucí potřeby šířky pásma.

Technologie řešila dva základní problémy: škálovatelnost šířky pásma a diferenciaci provozu. Komponenta multilink vyřešila problém škálovatelnosti tím, že umožnila 'přírůstkové' upgrady šířky pásma – operátoři mohli přidávat linky E1 do svazku s růstem provozu. Komponenta multiclass řešila problém QoS zavedením vrstvy správy provozu v rámci PPP, která dříve chyběla. Standardní PPP zacházelo se vším provozem stejně, což bylo nevhodné pro síť, kde signalizace RNC-Node B (kritická pro mobilitu) musí být doručena s vyšší prioritou a nižší latencí než datové pakety uživatelů. Definováním samostatných tříd ML/MC zajistilo, že řídicí provoz sítě může být chráněn, čímž se zlepšila celková spolehlivost a výkon sítě pro koncové uživatele. Jeho zavedení ve verzi 5 standardizovalo to, co by jinak mohly být proprietární řešení agregace spojů a QoS, a zajistilo tak interoperabilitu mezi různými dodavateli v transportní síti UTRAN.

## Klíčové vlastnosti

- Agreguje více fyzických spojů (např. E1, T1) do jediného logického kanálu za účelem zvýšení šířky pásma.
- Podporuje více tříd provozu (např. signalizaci, uživatelská data, O&M) pro diferencovanou QoS.
- Používá PPP Multilink Protocol (MP) pro fragmentaci, sekvencování a distribuci zátěže napříč spoji.
- Definuje Multiclass Protocol Data Unit (MC-PDU) pro identifikaci třídy provozu v rámcích.
- Poskytuje vyjednávací mechanismy prostřednictvím Multiclass Network Control Protocol (MC-NCP) během navazování spoje.
- Zvyšuje odolnost transportu přerozdělením provozu v případě selhání členského spoje.

## Definující specifikace

- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers

---

📖 **Anglický originál a plná specifikace:** [ML/MC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ml-mc/)
