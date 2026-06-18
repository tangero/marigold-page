---
slug: "ifri"
url: "/mobilnisite/slovnik/ifri/"
type: "slovnik"
title: "IFRI – Intra Frequency Reselection Indication"
date: 2025-01-01
abbr: "IFRI"
fullName: "Intra Frequency Reselection Indication"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ifri/"
summary: "Mechanismus v 5G NR, který poskytuje explicitní síťovou kontrolu nad chováním UE při přeskoku buňky na stejném kmitočtu. Zabránuje zbytečným přeskokům, čímž zvyšuje robustnost mobility a snižuje signa"
---

IFRI (indikace přeskoku uvnitř kmitočtu) je mechanismus 5G NR poskytující explicitní síťovou kontrolu nad procesem přeskoku buňky UE na stejném kmitočtu, aby se zabránilo zbytečným přeskokům a zvýšila robustnost mobility.

## Popis

Intra Frequency Reselection Indication (IFRI) je síťově řízená funkce mobility zavedená v 5G New Radio (NR) pro optimalizaci mobility v režimu idle a inactive. Funguje v rámci protokolové vrstvy Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)), konkrétně v blocích systémových informací ([SIB](/mobilnisite/slovnik/sib/)), jako jsou SIB2 a SIB4, a v dedikované signalizaci RRC, například ve zprávě RRCRelease. Síť vysílá parametr IFRI (buď jako logickou hodnotu, nebo výčtový typ) prostřednictvím broadcastu nebo unicastu, aby pokynula uživatelskému zařízení (UE), zda smí provádět měření a procedury přeskoku buňky na aktuálním servisním kmitočtu. Když je IFRI nastaveno do restriktivního stavu (např. 'nepovoleno'), je UE nuceno setrvat v aktuální buňce bez pokusu o přeskok uvnitř kmitočtu, a to i v případě, že jsou splněna běžná kritéria měření (např. S-kritérium). Tím se přebíjí autonomní algoritmus přeskoku buňky UE, který tradičně závisel výhradně na naměřeném výkonu ([RSRP](/mobilnisite/slovnik/rsrp/)) nebo kvalitě ([RSRQ](/mobilnisite/slovnik/rsrq/)) referenčního signálu v porovnání s broadcastovanými prahy.

Hlavní architektonická role IFRI je v rádiové přístupové síti (RAN), kterou řídí gNB. Funkce Radio Resource Management ([RRM](/mobilnisite/slovnik/rrm/)) gNB vyhodnocuje síťové podmínky – jako jsou požadavky na vyrovnávání zátěže, stabilitu buňky nebo přítomnost řezů pro ultra spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) – aby rozhodla, kdy IFRI uplatnit. Indikace je následně vložena do příslušného pole mobility control information v příslušné RRC zprávě. Po přijetí IFRI entita RRC v UE interpretuje tento příkaz a odpovídajícím způsobem nakonfiguruje nižší vrstvy (Layer 1 a Layer 2), což může vést např. k vypnutí měřicích mezer pro intra-frequency měření nebo k ignorování seznamů sousedních buněk na stejném kmitočtu. Tím je zajištěno, že UE zůstane ukotveno ke konkrétní buňce, což je klíčové pro zachování kontinuity relace u určitých služeb nebo pro potřeby síťového plánování.

Fungování IFRI je úzce propojeno s dalšími mechanismy mobility, jako je blokování buňky (cell barring) nebo rezervace buňky. Zatímco cell barring úplně zakazuje přístup, IFRI je granularnější selektivně omezuje pouze přeskok, zatímco normální procedury v režimu camped zůstávají povoleny. Funguje ve spojení s kontrolami přeskoku mezi kmitočty a mezi rádiovými technologiemi (inter-RAT), což síti umožňuje přesně směrovat provoz. Například ve scénáři s makro buňkou a podkladovými small buňkami na stejném kmitočtu může síť použít IFRI, aby zabránila ping-pong efektu UE mezi small buňkami, čímž se sníží počet požadavků na obnovení RRC spojení a šetří se energie baterie UE. Tato funkce je klíčovým prvkem pro rozšířenou síťově řízenou mobilitu, přecházející od reaktivních rozhodnutí založených na měření k proaktivnímu, na politikách založenému síťovému řízení.

## K čemu slouží

IFRI bylo zavedeno za účelem řešení omezení čistě na měření založeného přeskoku buňky v 5G sítích, které může vést k suboptimální mobilitě. V dřívějších vydáních 3GPP (před Rel-17) se UE ve stavech [RRC](/mobilnisite/slovnik/rrc/)_IDLE nebo RRC_INACTIVE autonomně rozhodovalo přejít na lepší buňku na stejném kmitočtu na základě broadcastovaných parametrů, jako jsou Qrxlevmin a Sintrasearch. Tento decentralizovaný přístup, byť jednoduchý, často vedl k nadměrnému počtu přeskoků (ping-pong) v hustých městských nebo heterogenních síťových strukturách, což způsobovalo zvýšenou signalizační zátěž, vyšší spotřebu baterie a potenciální přerušení služeb. Síť měla omezenou přímou kontrolu nad stabilizací hranic buněk nebo nad prioritizací určitých buněk pro specifické typy provozu.

Zavedení IFRI v Rel-17 poskytuje síti explicitní signalizaci, která přebíjí autonomii UE při přeskoku uvnitř kmitočtu. Tím se řeší problémy spojené s robustností mobility, zejména u služeb vyžadujících stabilní připojení k buňce, jako jsou ty využívající síťové řezy (network slicing) pro průmyslový IoT nebo vozidlovou komunikaci. Zamezením zbytečných přeskoků IFRI snižuje počet přechodů mezi RRC stavy a procedur aktualizace polohy, čímž se snižuje signalizační režie v core síti. Také umožňuje operátorům implementovat sofistikovanější politiky směrování provozu a vyrovnávání zátěže, a zajistit tak, že UE zůstanou na buňkách, které jsou optimálně nakonfigurovány pro jejich předplacené služby nebo instance síťových řezů.

## Klíčové vlastnosti

- Síťově řízené přepsání autonomního přeskoku buňky UE uvnitř kmitočtu
- Signalizováno prostřednictvím bloků systémových informací (SIB) nebo dedikovaných RRC zpráv
- Aplikovatelné v obou stavech RRC_IDLE a RRC_INACTIVE
- Zvyšuje robustnost mobility snížením ping-pong přeskoků
- Snižuje signalizační režii a spotřebu energie UE
- Podporuje politiky směrování provozu a síťových řezů (network slicing)

## Definující specifikace

- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [IFRI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ifri/)
