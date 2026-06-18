---
slug: "scpir"
url: "/mobilnisite/slovnik/scpir/"
type: "slovnik"
title: "SCPIR – Sub Channel Power Imbalance Ratio"
date: 2025-01-01
abbr: "SCPIR"
fullName: "Sub Channel Power Imbalance Ratio"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/scpir/"
summary: "Měřicí parametr v GSM/EDGE rádiových přístupových sítích, který kvantifikuje nerovnováhu výkonu mezi subkanály v konfiguraci s více časovými sloty. Je klíčový pro zajištění správného výkonu vysílače a"
---

SCPIR je měřicí parametr v GSM/EDGE, který kvantifikuje nerovnováhu výkonu mezi subkanály v konfiguraci s více časovými sloty, aby bylo zajištěno správné fungování vysílače a soulad s rádiovými požadavky.

## Popis

Sub Channel Power Imbalance Ratio (SCPIR) je technický parametr definovaný ve specifikacích GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové sítě ([GERAN](/mobilnisite/slovnik/geran/)), konkrétně pro vysílače podporující konfigurace s více časovými sloty, jako jsou ty používané v Enhanced Data Rates for GSM Evolution (EDGE) a General Packet Radio Service ([GPRS](/mobilnisite/slovnik/gprs/)). Působí na fyzické vrstvě a kvantifikuje relativní rozdíl výkonu mezi aktivními časovými sloty (subkanály) přidělenými jedné mobilní stanici nebo základnové stanici. Parametr se měří jako poměr, vyjádřený v decibelech (dB), výkonu v referenčním subkanálu k výkonu v jiném subkanálu ve stejném rádiovém kmitočtovém kanálu a přidělení s více sloty. Toto měření se provádí za specifických testovacích podmínek stanovených v konformních specifikacích, aby bylo zajištěno, že funkce řízení výkonu a tvarování burst vysílače fungují správně ve všech přidělených časových slotech.

Z architektonického hlediska je SCPIR vázán na výkonový zesilovač vysílače a příslušné řídicí obvody. Při provozu s více sloty musí jeden vysílač rychle přepínat úrovně výkonu mezi po sobě jdoucími časovými sloty, které mohou používat různá modulační schémata (např. [GMSK](/mobilnisite/slovnik/gmsk/) pro GSM, [8-PSK](/mobilnisite/slovnik/8-psk/) pro EDGE) nebo podléhat různým příkazům pro řízení výkonu. Vysílač musí pro každý burst udržovat stabilní a řízený výstupní výkon. SCPIR definuje přípustnou toleranci pro jakoukoli odchylku výkonu mezi těmito bursty. Nadměrná nerovnováha může vést ke zhoršenému výkonu přijímače na druhém konci spoje, zvýšené míře bitových chyb a potenciálnímu rušení sousedních kanálů nebo časových slotů.

Úloha SCPIR v síti je především v oblasti testování shody a zajišťování kvality. Nejde o dynamicky signalizovaný parametr, ale o statický požadavek, který zařízení musí splňovat. Testovací zařízení měří SCPIR během typových zkoušek nebo výrobních testů, aby ověřilo, že konstrukce vysílače zvládá rychlé změny výkonu vyžadované pro efektivní služby paketových dat. Tím, že standard zajišťuje nízkou a řízenou nerovnováhu výkonu, zaručuje, že výhody provozu s více sloty – konkrétně vyšší datový propust – nejsou narušeny špatnou linearitou vysílače nebo přechodovými jevy. Jeho specifikace pomáhá udržovat celkovou kmitočtovou účinnost sítě a koexistenci různých služeb na stejném nosiči.

## K čemu slouží

SCPIR byl zaveden, aby řešil specifické výzvy vysílačů vzniklé vývojem GSM do podoby paketově přepínané sítě schopné provozu s více časovými sloty. Před zavedením [GPRS](/mobilnisite/slovnik/gprs/) a [EDGE](/mobilnisite/slovnik/edge/) používalo GSM primárně jednoslotový okruhově přepínaný hlas, kde byl výkon vysílače pro jeden časový slot relativně konstantní. Zavedení konfigurací s více sloty pro vyšší datové rychlosti znamenalo, že jeden vysílač musel obsluhovat po sobě jdoucí časové sloty, potenciálně s různými úrovněmi výkonu kvůli řízení výkonu nebo různým modulačním schématům vyžadujícím různý poměr špičkového a průměrného výkonu. Bez definované metriky by nadměrné skoky výkonu mezi sloty mohly zkreslit signál, způsobit rušení a snížit efektivní datovou rychlost.

Vytvoření SCPIR poskytlo standardizovaný, měřitelný limit pro tuto změnu výkonu mezi sloty. Vyřešilo problém zajištění linearity vysílače a rychlosti přepínání kvantifikovatelným způsobem, což bylo nezbytné pro interoperabilitu mezi síťovými zařízeními od různých dodavatelů a pro zaručení konzistentního uživatelského zážitku u vysokorychlostních datových služeb. Formalizovalo klíčový požadavek na výkon fyzické vrstvy, který podporoval spolehlivost EDGE a zajišťoval, že teoretické zvýšení datové rychlosti bylo realizováno v praxi s robustním výkonem rádiového spoje.

## Klíčové vlastnosti

- Kvantifikuje rozdíl výkonu mezi časovými sloty v konfiguraci s více sloty
- Vyjádřen jako poměr v decibelech (dB)
- Klíčový parametr pro testování shody vysílače
- Zajišťuje stabilitu řízení výkonu při rychlém přepínání časových slotů
- Podporuje výkon služeb paketových dat EDGE a GPRS
- Definován za specifických testovacích podmínek v konformních specifikacích RF

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TS 45.005** (Rel-19) — GSM RF Requirements for MS and BSS
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity
- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [SCPIR na 3GPP Explorer](https://3gpp-explorer.com/glossary/scpir/)
