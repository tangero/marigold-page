---
slug: "bcc"
url: "/mobilnisite/slovnik/bcc/"
type: "slovnik"
title: "BCC – Base Transceiver Station Colour Code"
date: 2025-01-01
abbr: "BCC"
fullName: "Base Transceiver Station Colour Code"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bcc/"
summary: "3bitový identifikátor používaný v sítích GSM k rozlišení kolidujících základnových převaděčových stanic (BTS), které sdílejí stejný kód identity základnové stanice (BSIC). Zabraňuje interferencím a za"
---

BCC je 3bitový identifikátor používaný v sítích GSM k rozlišení kolidujících základnových převaděčových stanic (BTS) sdílejících stejný kód identity základnové stanice (BSIC), který předchází interferencím a zajišťuje správné předávání hovoru.

## Popis

BCC (Base Transceiver Station Colour Code – Barevný kód základnové převaděčové stanice) je základní součástí identifikace a řízení interference v GSM síti. Tvoří dolní 3 bity 6bitového kódu identity základnové stanice ([BSIC](/mobilnisite/slovnik/bsic/)), kde horní 3 bity představují Barevný kód sítě ([NCC](/mobilnisite/slovnik/ncc/)). BCC konkrétně identifikuje jednotlivé základnové převaděčové stanice ([BTS](/mobilnisite/slovnik/bts/)) v dané geografické oblasti, kde může více stanic BTS sdílet stejné frekvenční pásmo nebo být v těsné blízkosti. Toto 3bitové kódování umožňuje až 8 různých identifikátorů BTS (0–7) v rámci stejné domény NCC.

Z provozního hlediska BCC spolupracuje s kanálem Broadcast Control Channel ([BCCH](/mobilnisite/slovnik/bcch/)) a Synchronization Channel (SCH), aby umožnilo mobilním stanicím rozlišit sousední základnové stanice. Když mobilní stanice provádí měření okolních buněk, dekóduje BSIC ze schránky SCH a extrahuje složky NCC i BCC. Část BCC konkrétně pomáhá mobilní stanici rozlišit různé BTS, i když sdílejí stejnou frekvenci nebo když se mobil nachází v oblasti s hustou koncentrací buněk. To je zvláště důležité během procedur předávání hovoru, kde musí mobil přesně identifikovat cílovou buňku.

Primární technickou funkcí BCC je zamezení interference a identifikace buňky. Ve frekvenčních reuse vzorcích běžných v GSM sítích může být stejná frekvence znovu použita v různých buňkách v rámci stejné geografické oblasti. BCC zajišťuje, že když mobilní stanice hlásí měření síti, může jednoznačně identifikovat, kterou konkrétní BTS měří, i když více BTS používá stejnou frekvenci. Tím se předchází nesprávným předáním hovoru a snižuje interference. BCC je nepřetržitě vysílán jako součást BSIC v každém časovém slotu SCH, což umožňuje mobilním stanicím neustále monitorovat a identifikovat sousední buňky.

Z architektonického pohledu je BCC konfigurován na úrovni BTS a spravován prostřednictvím Operations and Maintenance Center ([OMC](/mobilnisite/slovnik/omc/)). Plánovači sítě pečlivě přiřazují hodnoty BCC, aby se předešlo kolizím v dosahu interference, obvykle podle specifických reuse vzorců podobných frekvenčnímu plánování. BCC spolupracuje s dalšími identifikačními parametry, jako je Cell Global Identity ([CGI](/mobilnisite/slovnik/cgi/)) a Location Area Code ([LAC](/mobilnisite/slovnik/lac/)), a poskytuje tak komplexní identifikaci buňky. Zatímco CGI poskytuje globální jedinečnost, BCC poskytuje lokální diferenciaci nezbytnou pro každodenní správu mobility a řízení interference.

## K čemu slouží

BCC byl vytvořen, aby řešil základní problémy s interferencí a identifikací v raných nasazeních GSM sítí. Jak se buněčné sítě rozšiřovaly a hustota buněk zvyšovala, často více základnových převaděčových stanic fungovalo v těsné blízkosti a někdy sdílelo frekvenční alokace kvůli omezenosti spektra. Bez mechanismu k rozlišení kolidujících nebo sousedících [BTS](/mobilnisite/slovnik/bts/) používajících podobné parametry by mobilní stanice zápasily s přesnou identifikací cílových buněk pro předání hovoru, což by vedlo k přerušeným hovorům a špatnému výkonu sítě.

Před standardizovanými identifikačními schématy, jako je BSIC s jeho složkou BCC, čelily rané buněčné systémy významným výzvám s nejednoznačnou identifikací buněk. Mobilní stanice mohly špatně interpretovat měření z různých základnových stanic jako pocházející ze stejného zdroje, což způsobovalo nesprávná rozhodnutí o předání hovoru a interference. BCC tento problém konkrétně řeší tím, že poskytuje lokálně jedinečný identifikátor, který v kombinaci s NCC vytváří úplný BSIC, jenž je jedinečný v dané geografické oblasti. To umožňuje přesnou diskriminaci buněk i v hustých městských nasazeních s vysokým frekvenčním reuse.

Historický kontext vývoje BCC přímo souvisí s potřebou robustní správy mobility v GSM sítích při jejich škálování. Když operátoři nasazovali více buněk pro zvýšení kapacity, rostla pravděpodobnost konfliktů identifikace BTS. 3bitová struktura BCC byla navržena tak, aby vyvážila granularitu identifikace s režií signalizace, a poskytla dostatek různých kódů (8 na NCC) pro typické scénáře nasazení, přičemž identifikátor zůstal kompaktní pro efektivní vysílání. Toto řešení umožnilo nasazení buněk s vysokou hustotou, které charakterizovalo vývoj sítí 2G, a položilo základy pro pozdější technologie 3GPP.

## Klíčové vlastnosti

- 3bitový identifikátor umožňující 8 různých hodnot (0–7)
- Tvoří spodní část 6bitového kódu identity základnové stanice (BSIC)
- Umožňuje rozlišení mezi kolidujícími základnovými převaděčovými stanicemi
- Zabraňuje interferenci ve scénářích s frekvenčním reuse
- Nezbytný pro přesné rozhodování o předání hovoru
- Nepřetržitě vysílán ve schránkách Synchronization Channel (SCH)

## Související pojmy

- [BSIC – Base transceiver Station Identity Code](/mobilnisite/slovnik/bsic/)
- [NCC – Network (PLMN) Colour Code](/mobilnisite/slovnik/ncc/)
- [BTS – Base Transceiver Station](/mobilnisite/slovnik/bts/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 44.069** (Rel-19) — Broadcast Call Control (BCC) Protocol

---

📖 **Anglický originál a plná specifikace:** [BCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/bcc/)
