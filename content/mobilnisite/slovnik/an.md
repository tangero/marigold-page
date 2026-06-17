---
slug: "an"
url: "/mobilnisite/slovnik/an/"
type: "slovnik"
title: "AN – Access Network"
date: 2025-01-01
abbr: "AN"
fullName: "Access Network"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/an/"
summary: "Přístupová síť (AN) je část telekomunikační sítě, která spojuje koncová uživatelská zařízení s páteřní sítí. Poskytuje rádiovou a fyzickou infrastrukturu pro bezdrátovou komunikaci, zajišťuje správu r"
---

AN je část telekomunikační sítě, která spojuje koncová uživatelská zařízení s páteřní sítí, poskytuje rádiovou infrastrukturu pro bezdrátovou komunikaci a zajišťuje správu rádiových prostředků a mobilitu.

## Popis

Přístupová síť (AN) představuje klíčovou infrastrukturu, která zprostředkovává bezdrátové spojení mezi uživatelským zařízením (UE) a páteřní sítí v systémech 3GPP. Je odpovědná za správu rádiového rozhraní, což zahrnuje všechny funkce související s rádiovým přenosem a příjmem. Architektonicky se AN nachází mezi UE a bránami řídicí a uživatelské roviny páteřní sítě. Jejím hlavním úkolem je vytvářet, udržovat a uvolňovat rádiové přenosové kanály, což jsou logické kanály přenášející uživatelská data a signalizační informace přes rozhraní vzdušného rozhraní. AN dynamicky spravuje rádiové prostředky, přiděluje šířku pásma, řídí výkon a provádí procedury předávání hovoru, aby zajistila plynulou mobilitu při pohybu uživatelů mezi buňkami.

Ve specifikacích 3GPP je AN implementována různě v jednotlivých generacích, ale zachovává si svůj základní účel. V UMTS (3G) je AN známá jako UTRAN (UMTS Terrestrial Radio Access Network), která se skládá ze základnových stanic Node B a řadičů rádiové sítě (RNC). V LTE (4G) je to [E-UTRAN](/mobilnisite/slovnik/e-utran/) (Evolved UTRAN), který architekturu zjednodušil odstraněním RNC a sloučením jeho funkcí do eNodeB (evolved Node B). V 5G NR je AN tvořena NG-RAN (Next Generation Radio Access Network), která se skládá z gNB (next-generation Node B) a volitelně ng-eNB pro nestandalone provoz s LTE. AN každé generace implementuje specifické technologie vzdušného rozhraní (např. WCDMA, [OFDMA](/mobilnisite/slovnik/ofdma/)) a protokoly, aby splnila rostoucí výkonnostní požadavky.

AN funguje prostřednictvím několika klíčových funkčních komponent. Vrstva řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) spravuje navazování spojení, mobilitu a vysílání systémových informací. Vrstva konvergenčního protokolu paketových dat (PDCP) zajišťuje kompresi hlaviček, šifrování a ochranu integrity. Vrstva řízení rádiového spoje (RLC) spravuje segmentaci, opakovaný přenos a doručování ve správném pořadí. Vrstva řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) plánuje data, spravuje hybridní automatické opakování žádosti ([HARQ](/mobilnisite/slovnik/harq/)) a multiplexuje logické kanály. Nakonec fyzická vrstva (PHY) provádí kódování, modulaci a vlastní přenos přes rádiové spektrum. Společně tyto vrstvy zajišťují spolehlivý, efektivní a bezpečný přenos dat přes inherentně náročné bezdrátové prostředí.

Výkon AN přímo ovlivňuje klíčové metriky sítě, jako je propustnost dat, latence, pokrytí a kapacita. Rozhraní s páteřní sítí je zajištěno standardizovanými rozhraními: rozhraním Iu v UMTS, rozhraním S1 v LTE a rozhraním [NG](/mobilnisite/slovnik/ng/) v 5G. Tato rozhraní oddělují signalizaci řídicí roviny (např. k [MME](/mobilnisite/slovnik/mme/) nebo [AMF](/mobilnisite/slovnik/amf/)) od dat uživatelské roviny (např. k SGW nebo UPF). AN také hraje zásadní roli v řízení a optimalizaci sítě, poskytuje měření a výkonnostní data systému pro podporu provozu (OSS) pro monitorování, správu poruch a plánování rádiové sítě. Její návrh je průběžně optimalizován, aby podporoval nové služby, od hlasu a mobilního širokopásmového připojení až po hromadný IoT a ultra-spolehlivou komunikaci s nízkou latencí.

## K čemu slouží

Přístupová síť existuje proto, aby překlenula propast mezi mobilními zařízeními a servisní infrastrukturou páteřní sítě. Jejím základním účelem je poskytnout všudypřítomné bezdrátové pokrytí a kapacitu, což umožňuje mobilní komunikaci. Řeší problém připojení potenciálně obrovského počtu geograficky rozptýlených, mobilních uživatelů k centralizované síti s využitím sdíleného, omezeného a rušení náchylného prostředku: rádiového spektra. Bez AN by mobilní zařízení neměla prostředky k navázání komunikačního spojení, což by znemožnilo existenci celulárních sítí.

Historicky byl vývoj AN hnán potřebou podporovat nové služby s rostoucími výkonnostními nároky. Rané celulární sítě (1G, 2G) se soustředily na přepojování okruhů pro hlas, což vyžadovalo AN schopné spravovat frekvenční kanály a základní předávání hovoru. Zavedení přepojování paketů pro data s 3G si vyžádalo složitější architektury AN (UTRAN) pro zvládnutí proměnných datových toků a kvality služeb (QoS). Přechod na plně IP, vysokorychlostní data v 4G vedl ke zploštělé architektuře AN (E-UTRAN) za účelem snížení latence a zlepšení efektivity. Každá generace řešila omezení té předchozí: 3G zlepšilo datové toky oproti 2G, 4G snížilo složitost a latenci oproti 3G a 5G je navrženo pro extrémní flexibilitu, aby podporovalo rozmanité případy užití přesahující mobilní širokopásmové připojení.

Vytvoření a průběžné vylepšování AN je motivováno základním podnikáním mobilních operátorů: poskytovat spolehlivé, vysoce kvalitní služby konektivity. Řeší technické výzvy, jako je útlum šíření signálu, vícesté rozpětí, ko-kanálové rušení a mobilita uživatelů. Efektivní správou rádiového rozhraní AN maximalizuje spektrální účinnost (bitů za sekundu na Hertz), prodlužuje výdrž baterie pomocí inteligentního řízení výkonu a zajišťuje kontinuitu služeb během pohybu. Je to nejviditelnější a nejnákladnější část sítě na nasazení a údržbu, což činí její návrh a optimalizaci prvořadými pro komerční úspěch jakéhokoli mobilního operátora.

## Klíčové vlastnosti

- Správa rádiových prostředků (RRM) pro dynamické přidělování spektra a výkonu
- Správa mobility podporující předávání hovoru (intra- a inter-RAT) pro plynulou konektivitu
- Vícevrstvý zásobník protokolů (RRC, PDCP, RLC, MAC, PHY) pro spolehlivý přenos dat
- Rozhraní k páteřní síti (např. S1, NG) oddělující funkce řídicí a uživatelské roviny
- Podpora více technologií rádiového přístupu (např. 5G NR, LTE, WCDMA) napříč generacemi
- Poskytování měření a dat pro provoz, správu a údržbu sítě (OAM)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 26.091** (Rel-19) — AMR Error Concealment Procedure
- **TS 26.093** (Rel-19) — SCR operation of AMR codec for UMTS
- **TS 26.191** (Rel-19) — AMR-WB Error Concealment Procedure
- **TS 26.193** (Rel-19) — AMR-WB Source Controlled Rate (SCR) Operation
- **TR 26.919** (Rel-19) — Study on 5G Conversational Media Handling
- **TR 28.808** (Rel-17) — 5G satellite integration management study
- **TR 28.841** (Rel-18) — Technical Report on IoT NTN Enhancements
- **TS 29.276** (Rel-19) — EPS S101/S121/S103 Interfaces Stage 3
- **TS 29.890** (Rel-16) — CT3 5G System Technical Report
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [AN na 3GPP Explorer](https://3gpp-explorer.com/glossary/an/)
