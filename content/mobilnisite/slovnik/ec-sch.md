---
slug: "ec-sch"
url: "/mobilnisite/slovnik/ec-sch/"
type: "slovnik"
title: "EC-SCH – Extended Coverage Synchronization Channel"
date: 2025-01-01
abbr: "EC-SCH"
fullName: "Extended Coverage Synchronization Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ec-sch/"
summary: "Downlinkový vysílací kanál v GSM/EDGE, který poskytuje časovou a frekvenční synchronizaci pro IoT zařízení ve scénářích s rozšířeným pokrytím. Vysílá opakované synchronizační blesky obsahující kód ide"
---

EC-SCH je downlinkový vysílací kanál v GSM/EDGE, který poskytuje časovou a frekvenční synchronizaci pro IoT zařízení ve scénářích s rozšířeným pokrytím.

## Popis

Extended Coverage Synchronization Channel (EC-SCH) je fyzický downlinkový vysílací kanál definovaný ve standardech GSM/[EDGE](/mobilnisite/slovnik/edge/) (3GPP TS 44.060) pro provoz Extended Coverage GSM (EC-GSM). Je to klíčový kanál v rámci sady funkcí Cellular Internet of Things (CIoT), zodpovědný za poskytování informací o časové a frekvenční synchronizaci uživatelskému zařízení (UE). Předtím, než může IoT zařízení číst systémové informace, monitorovat volání nebo zahájit náhodný přístup, se musí nejprve synchronizovat se sítí – tedy sladit svůj interní hodinový a frekvenční referenční signál s vysílající základnovou stanicí. EC-SCH je speciálně navržen tak, aby tuto synchronizaci umožnil i při výrazném útlumu signálu, s útlumy na dráze až do 164 dB, což je typické pro zařízení ve sklepích, hluboko v budovách nebo na samém okraji pokrytí buňky.

Architektonicky je EC-SCH logický kanál, který je mapován na specifické časové sloty v rámci struktury vícekanálového rámce GSM. Funguje vedle původního kanálu pro frekvenční korekci ([FCCH](/mobilnisite/slovnik/fcch/)) a synchronizačního kanálu ([SCH](/mobilnisite/slovnik/sch/)), ale používá odlišný, robustnější přenosový režim. Kanál vysílá známou bitovou sekvenci, Extended Coverage Synchronization Burst (EC-SB). Tento blesk je opakován vysílán slepým způsobem, což znamená, že síť jej vysílá nepřetržitě bez nutnosti zpětné vazby nebo znalosti o naslouchajících zařízeních. Vzor opakování je hustý a předvídatelný, což umožňuje zařízení hledat signál v čase a kombinovat energii z více blesků k dosažení úspěšné synchronizace. EC-SB nese základní informace: Reduced Frame Number ([RFN](/mobilnisite/slovnik/rfn/)) a Base Station Identity Code ([BSIC](/mobilnisite/slovnik/bsic/)). RFN poskytuje zařízení časování struktury rámce GSM, zatímco BSIC identifikuje síť a buňku.

Technický proces synchronizace zařízení prostřednictvím EC-SCH zahrnuje vícekrokový proces korelace a kombinování. Zařízení se zapne nebo vstoupí do nové oblasti pokrytí a začne hledat signál EC-SCH na určených kmitočtech nosné. Kvůli extrémně nízkému poměru signálu k šumu ([SNR](/mobilnisite/slovnik/snr/)) zařízení nedokáže dekódovat jednotlivý blesk. Místo toho provádí koherentní nebo nekoherentní kombinování přijímaného signálu z více opakovaných přenosů EC-SB. Korelací přijímaného signálu se známou sekvencí EC-SB napříč těmito kombinovanými opakováními může zařízení detekovat přítomnost kanálu, odhadnout přesné časování blesku (čímž sladí své časování) a určit posun kmitočtu nosné. Jakmile je časování získáno, může zařízení dekódovat informace BSIC a RFN. Tato synchronizace je základním krokem, který umožňuje zařízení následně demodulovat Extended Coverage Broadcast Control Channel ([EC-BCCH](/mobilnisite/slovnik/ec-bcch/)) pro příjem systémových informací a nakonec přistoupit k síti přes [EC-RACH](/mobilnisite/slovnik/ec-rach/) nebo naslouchat volání na EC-PCH.

## K čemu slouží

EC-SCH byl vytvořen, aby řešil základní předpoklad pro činnost v celulární síti: synchronizaci se sítí. Ve standardním GSM umožňuje synchronizační kanál (SCH) zařízením rychle se sladit s časováním sítě. Jeho návrh však předpokládá relativně dobré rádiové spojení. Pro IoT zařízení nasazená v náročných prostředích, která jsou cílem EC-GSM – jako jsou chytré měřiče za silnými zdmi, senzory ve venkovských šachtách nebo sledovací zařízení uvnitř kovových kontejnerů – je signál ze SCH často příliš slabý na to, aby byl detekován. Bez úspěšné synchronizace je zařízení vůči síti zcela slepé; nemůže určit hranice rámců, identifikovat buňku ani přistoupit k jakémukoli dalšímu síťovému postupu. To činilo stávající GSM sítě nepoužitelnými pro širokou škálu IoT aplikací vyžadujících hluboké pokrytí.

Vývoj EC-SCH byl motivován cílem 3GPP Release 13 vyvinout GSM v konkurenceschopnou technologii Cellular IoT. Primárním cílem bylo dosáhnout 20 dB zlepšení v rozpočtu spoje, kvantifikovaného jako maximální útlum na dráze (MCL) 164 dB. Synchronizace je první a nejcitlivější downlinkový postup, protože probíhá bez jakýchkoli předchozích znalostí. Pokud synchronizace selže, jsou všechna další vylepšení (jako EC-PCH nebo EC-RACH) bezpředmětná. EC-SCH to řeší použitím jednoduché, ale účinné techniky: neustálým opakováním robustní synchronizační sekvence. To dává zařízení dlouhý integrační čas na vytažení signálu z šumu, což efektivně vyměňuje čas za citlivost.

Před EC-GSM se zařízení v takto extrémních lokalitách prostě nemohla zaregistrovat na GSM síti. Alternativní necelaulární LPWAN technologie často používaly velmi pomalé, opakované synchronizační schémata, které GSM potřebovalo napodobit. EC-SCH poskytuje standardizovanou metodu optimalizovanou pro zařízení s omezeným výkonem. Slepý, opakovaný přenos znamená, že zařízení nepotřebuje žádat o pomoc se synchronizací; může synchronizaci dosáhnout autonomně nasloucháním. Tento návrh je zásadní pro životnost baterie, protože minimalizuje čas a výpočetní výkon potřebný pro počáteční hledání buňky. Tím, že zajišťuje spolehlivou synchronizaci v nejnáročnějších podmínkách, EC-SCH klade základní základy, díky nimž je celý systém EC-GSM životaschopný pro masivní IoT nasazení s hlubokým pokrytím.

## Klíčové vlastnosti

- Vysílá Extended Coverage Synchronization Burst (EC-SB) pomocí opakovaných, slepých přenosů pro zvýšení pokrytí
- Nese kritická synchronizační data: Reduced Frame Number (RFN) pro časování a Base Station Identity Code (BSIC) pro identifikaci buňky
- Umožňuje zařízením použít kombinování signálu z více blesků k dosažení synchronizace při velmi nízkém SNR (až do 164 dB MCL)
- Poskytuje základní časovou referenci potřebnou pro zařízení k následnému dekódování EC-BCCH a přístupu k dalším kanálům EC-GSM
- Funguje na předdefinovaných fyzických zdrojích v rámci struktury rámce GSM vyhrazených pro provoz EC-GSM
- Navržen pro autonomní provoz zařízení, nevyžaduje žádnou zpětnou vazbu sítě nebo pomoc pro počáteční synchronizační proces

## Související pojmy

- [EC-BCCH – Extended Coverage BroadCast CHannel](/mobilnisite/slovnik/ec-bcch/)
- [EC-PCH – Extended Coverage Paging Channel](/mobilnisite/slovnik/ec-pch/)
- [EC-RACH – Extended Coverage Random Access Channel](/mobilnisite/slovnik/ec-rach/)
- [BSIC – Base transceiver Station Identity Code](/mobilnisite/slovnik/bsic/)

## Definující specifikace

- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [EC-SCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ec-sch/)
