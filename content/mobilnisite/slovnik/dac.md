---
slug: "dac"
url: "/mobilnisite/slovnik/dac/"
type: "slovnik"
title: "DAC – Digital-to-Analogue Converter"
date: 2026-01-01
abbr: "DAC"
fullName: "Digital-to-Analogue Converter"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dac/"
summary: "Základní hardwarová komponenta, která převádí digitální signály na analogové průběhy pro přenos přes fyzická média. Umožňuje digitálnímu zpracování základního pásma komunikovat s analogovými řetězci v"
---

DAC je hardwarová komponenta, která převádí digitální signály na analogové průběhy pro přenos, což umožňuje digitálnímu zpracování základního pásma komunikovat s analogovými řetězci vysokofrekvenční části v vysílačích a přijímačích.

## Popis

Digital-to-Analogue Converter (DAC, číslicově-analogový převodník) je kritický integrovaný obvod pro smíšené signály, který transformuje diskrétní v čase a amplitudě digitální vzorky na spojité v čase a amplitudě analogové signály. V systémech 3GPP DAC fungují na rozhraní mezi jednotkami pro digitální zpracování základního pásma a analogovými vysokofrekvenčními ([RF](/mobilnisite/slovnik/rf/)) předkoncovými obvody, což umožňuje fyzický přenos digitálně zpracovaných informací přes bezdrátové kanály. Proces převodu zahrnuje rekonstrukci analogového průběhu z digitálních vzorků za použití technik, jako je tvarování impulsu, interpolační filtrace a analogová rekonstrukční filtrace, aby byly splněny přísné požadavky na spektrální masku a minimalizovaly se nežádoucí emise mimo pásmo.

Z architektonického hlediska jsou DAC v rádiovém zařízení 3GPP charakterizovány klíčovými výkonnostními parametry včetně rozlišení (bitové hloubky), vzorkovací frekvence, dynamického rozsahu bez nežádoucích složek (SFDR), poměru signálu k šumu ([SNR](/mobilnisite/slovnik/snr/)) a celkového harmonického zkreslení (THD). Vyšší modulační schémata jako 256-QAM a 1024-QAM v 5G NR vyžadují DAC s výjimečnou linearitou a nízkou hladinou vlastního šumu, aby byla zachována přesnost konstelace a minimalizována velikost chybového vektoru ([EVM](/mobilnisite/slovnik/evm/)). Moderní implementace DAC často zahrnují digitální předkompenzaci, tvarování šumu a pokročilé interpolační filtry pro optimalizaci výkonu při současném dosažení cílů energetické účinnosti.

Role DAC se rozprostírá jak do vysílacích, tak přijímacích řetězců. Ve vysílačích převádí digitálně modulované signály základního pásma do analogové podoby pro následné převedení na RF frekvence. V přijímačích může být použit ve zpětnovazebních drahách pro systémy digitální předkompenzace nebo v některých přijímacích architekturách. Výkon DAC přímo ovlivňuje klíčové systémové metriky včetně poměru úniku do sousedního kanálu ([ACLR](/mobilnisite/slovnik/aclr/)), velikosti chybového vektoru (EVM) a propustnosti. Jak se systémy 3GPP vyvíjely od 4G LTE k 5G NR, požadavky na DAC se staly stále přísnějšími, aby podpořily širší šířky pásma, vyšší kmitočty nosné a složitější modulační schémata při zachování spektrální účinnosti a souladu s regulacemi.

Mezi implementační aspekty patří citlivost na chvění hodinového signálu (jitter), které ovlivňuje fázový šum a v konečném důsledku systémové EVM; tepelné řízení, protože vysokorychlostní DAC generují značné teplo; a integrace s komponentami digitální předkoncové části ([DFE](/mobilnisite/slovnik/dfe/)). Pokročilé architektury DAC využívají techniky, jako je segmentované řízení proudu, přepínání s návratem k nule a vícejádrová interpolace, aby dosáhly potřebného výkonu pro milimetrové vlny v aplikacích 5G. Specifikace DAC jsou pečlivě vyvažovány s požadavky na analogově-číslicové převodníky ([ADC](/mobilnisite/slovnik/adc/)), aby byla zachována integrita signálového řetězce od konce ke konci přes rádiové rozhraní.

## K čemu slouží

DAC existuje pro propojení digitální a analogové domény v bezdrátových komunikačních systémech, což umožňuje praktickou implementaci sofistikovaných algoritmů digitálního zpracování signálu v reálném rádiovém zařízení. Jak se standardy 3GPP vyvíjely od 2G GSM k 5G NR, průmysl přešel k softwarově definovaným rádiím a digitálnímu zpracování základního pásma, aby dosáhl větší flexibility, programovatelnosti a výkonu. Fyzický přenosový prostředek však zůstává analogový, což vyžaduje vysoce věrný převod mezi těmito doménami.

Historicky rané celulární systémy používaly převážně analogové komponenty s omezeným digitálním zpracováním. Přechod k digitálním systémům ve 2G GSM odhalil potřebu přesných DAC pro převod digitálně zpracovaných hlasových signálů do analogové podoby pro [RF](/mobilnisite/slovnik/rf/) přenos. Každá následující generace zaváděla složitější digitální modulační schémata ([QPSK](/mobilnisite/slovnik/qpsk/), 16-QAM, 64-QAM atd.) a širší šířky pásma, což kladlo rostoucí nároky na výkon DAC. Mezi omezení dřívějších technologií DAC patřilo nedostatečné rozlišení pro vyšší modulační řády, nedostatečné vzorkovací frekvence pro širší šířky pásma a nadměrná spotřeba energie pro mobilní aplikace.

Vytvoření a neustálé zlepšování technologie DAC řeší základní výzvy v bezdrátové komunikaci: zachování integrity signálu během procesu číslicově-analogového převodu, minimalizaci zkreslení, které degraduje výkon systému, a umožnění praktické implementace pokročilých technik digitálního zpracování signálu. Bez vysoce výkonných DAC by nebylo možné realizovat sofistikovaná modulační schémata, techniky vícenásobného přístupu a vylepšení spektrální účinnosti definované ve standardech 3GPP v praktickém rádiovém zařízení. DAC tedy slouží jako nezbytný prostředek pro vývoj celulární technologie od systémů zaměřených na hlas k širokopásmovým datovým sítím podporujícím rozmanité služby a aplikace.

## Klíčové vlastnosti

- Převádí vzorky digitálního základního pásma na analogové průběhy pro RF přenos
- Podporuje převod s vysokým rozlišením (typicky 12-16 bitů) pro složitá modulační schémata
- Pracuje se vzorkovacími frekvencemi přesahujícími Nyquistovy požadavky pro signály s širokým pásmem
- Zahrnuje interpolační a rekonstrukční filtry pro splnění spektrálních masek
- Poskytuje nízkou hladinu vlastního šumu a vysokou linearitu pro minimalizaci EVM a ACLR
- Umožňuje digitální předkompenzaci prostřednictvím zpětnovazebních drah ve vysílacích architekturách

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks
- **TS 26.115** (Rel-19) — 3GPP TS 26115: Echo Control Requirements
- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TR 38.877** (Rel-18) — Technical Report
- **TS 43.050** (Rel-19) — GSM Transmission Planning for Speech Services

---

📖 **Anglický originál a plná specifikace:** [DAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/dac/)
