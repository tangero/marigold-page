---
slug: "osr"
url: "/mobilnisite/slovnik/osr/"
type: "slovnik"
title: "OSR – Observation Space Representation"
date: 2025-01-01
abbr: "OSR"
fullName: "Observation Space Representation"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/osr/"
summary: "OSR je technika určování polohy v 5G NR, která definuje matematické reprezentace pozorovacích prostorů pro odhad polohy, čímž zvyšuje přesnost v náročných prostředích. Modeluje signálová měření, jako"
---

OSR je technika určování polohy v 5G NR, která definuje matematické reprezentace pozorovacích prostorů, modeluje signálové měření jako čas příchodu (time-of-arrival) za účelem zvýšení přesnosti odhadu polohy.

## Popis

Observation Space Representation (OSR, reprezentace pozorovacího prostoru) je pokročilá metodologie určování polohy definovaná ve specifikaci 3GPP 37.355, zavedená jako součást 5G New Radio (NR) pro zlepšení služeb založených na poloze. Zahrnuje matematické modelování pozorovacích prostorů, což jsou abstraktní domény zahrnující všechna možná měření z rádiových signálů používaná pro odhad polohy zařízení. OSR funguje tak, že reprezentuje měření jako čas příchodu ([TOA](/mobilnisite/slovnik/toa/)), rozdíl času příchodu (TDOA), úhel příchodu ([AOA](/mobilnisite/slovnik/aoa/)) a výkon přijatého referenčního signálu ([RSRP](/mobilnisite/slovnik/rsrp/)) ve strukturovaném vektorovém prostoru, což umožňuje přesnější a robustnější výpočty polohy. Tento přístup je obzvláště cenný v prostředích bez přímé viditelnosti ([NLOS](/mobilnisite/slovnik/nlos/)) nebo v hustě zastavěných městských oblastech, kde tradiční metody určování polohy mohou trpět vícecestným šířením a degradací signálu.

Z architektonického hlediska se OSR integruje s architekturou určování polohy v 5G, která zahrnuje síťové entity jako funkci správy polohy ([LMF](/mobilnisite/slovnik/lmf/)) a uživatelské zařízení (UE), které sbírají měřená data. Mezi klíčové komponenty OSR patří pozorovací vektory agregující více parametrů signálu, kovarianční matice kvantifikující nejistoty měření a transformační funkce mapující nezpracovaná data do pozorovacího prostoru. Proces začíná sběrem rádiových měření ze strany UE nebo základnových stanic (gNodeB), která jsou následně formátována podle definic OSR a přenášena do LMF. LMF používá tyto reprezentace v algoritmech, jako je odhad metodou nejmenších čtverců nebo Bayesovská filtrace, pro výpočet odhadů polohy, přičemž zohledňuje chyby a zvyšuje spolehlivost. OSR také podporuje hybridní určování polohy kombinací dat z 5G NR s jinými systémy, jako je [GPS](/mobilnisite/slovnik/gps/) nebo Wi-Fi, a vytváří tak jednotný pozorovací rámec.

V provozu OSR zvyšuje přesnost určování polohy tím, že poskytuje standardizovaný způsob zpracování šumu měření a korelací, což je klíčové pro vysoce přesné aplikace jako tísňové služby (např. E911), průmyslovou automatizaci a komunikaci mezi vozidly. Umožňuje funkce jako kvantifikace nejistoty, kdy jsou odhadům polohy přiřazeny úrovně spolehlivosti, což napomáhá rozhodování pro služby závislé na poloze. Role OSR v sítích 5G je klíčová s rostoucí poptávkou po určování polohy s přesností na úrovni pod metr ve scénářích, jako jsou tovární robotika nebo rozšířená realita, kde tradiční metody selhávají. Tím, že abstrahuje složitosti měření do koherentního matematického modelu, OSR usnadňuje interoperabilitu mezi různými technologiemi určování polohy a připravuje cestu pro budoucí vylepšení v Release 16 a novějších, jako je určování polohy založené na postranním spoji (sidelink).

## K čemu slouží

OSR byl vyvinut k řešení omezení stávajících technik určování polohy v systémech 4G a raného 5G, které často zápasily s přesností a spolehlivostí v komplexních rádiových prostředích. Před jeho zavedením poskytovaly metody jako cell-ID nebo asistovaný [GPS](/mobilnisite/slovnik/gps/) základní odhady polohy, ale byly nedostatečné pro nové případy užití vyžadující vysokou přesnost, jako jsou autonomní vozidla nebo vnitřní navigace. Nárůst hustoty sítě a použití vyšších kmitočtových pásem v 5G NR přinesly nové výzvy, včetně výrazných vícecestných jevů a proměnlivých podmínek signálu, což si vyžádalo sofistikovanější přístup k reprezentaci měření.

Tato technologie řeší problémy spojené s nejednoznačností měření a šířením chyb tím, že poskytuje formalizovaný pozorovací prostor, který standardizuje způsob zpracování dat o poloze napříč síťovými prvky. To umožňuje lepší fúzi více typů měření a zvyšuje odolnost vůči zkreslením prostředí. Historicky bylo vytvoření OSR v Release 15 motivováno cíli 3GPP zlepšit schopnosti určování polohy jako součást širšího portfolia služeb 5G, aby podpořilo regulatorní požadavky pro tísňové služby a umožnilo nové komerční aplikace. Navazuje na dřívější práci v určování polohy v LTE, ale zavádí flexibilnější a škálovatelnější rámec, který řeší potřebu služeb určování polohy s nízkou latencí a vysokou přesností v různých scénářích nasazení.

## Klíčové vlastnosti

- Matematická reprezentace pozorovacích prostorů pro měření určování polohy
- Podpora více typů měření včetně TOA, TDOA, AOA a RSRP
- Kvantifikace nejistoty a modelování kovariance chyb
- Integrace s architekturou určování polohy 5G NR a LMF
- Možnosti hybridního určování polohy kombinujícího 5G s jinými technologiemi
- Vylepšená přesnost v prostředích NLOS a v hustě zastavěných městských oblastech

## Související pojmy

- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)

---

📖 **Anglický originál a plná specifikace:** [OSR na 3GPP Explorer](https://3gpp-explorer.com/glossary/osr/)
