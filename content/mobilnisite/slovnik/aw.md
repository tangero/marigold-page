---
slug: "aw"
url: "/mobilnisite/slovnik/aw/"
type: "slovnik"
title: "AW – Average Window"
date: 2025-01-01
abbr: "AW"
fullName: "Average Window"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/aw/"
summary: "Časové průměrovací okno používané v řízení politik a účtování (PCC) v 5G sítích ke zprůměrování měření provozu a vynucení QoS politik. Vypočítává průměrné datové rychlosti za definované období, čímž z"
---

AW je časové průměrovací okno používané v řízení politik a účtování (PCC) v 5G sítích ke zprůměrování měření provozu výpočtem průměrných datových rychlostí za definované období, čímž se zabrání náhlým aktivacím politik způsobeným přechodnými špičkami.

## Popis

Průměrovací okno (Average Window, AW) je základní parametr v architektuře řízení politik a účtování ([PCC](/mobilnisite/slovnik/pcc/)) v 5G, definovaný v 3GPP TS 29.513. Funguje jako konfigurovatelný časový interval, typicky udávaný v sekundách, za který se průměrují konkrétní měření provozu – například datové rychlosti v uplinku a downlinku. Toto průměrování není prostým aritmetickým průměrem, ale kontinuálním výpočtem s posuvným oknem, který provádí Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) nebo User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) na základě reportů o reálném využití. Základní mechanismus zahrnuje monitorování paketových toků asociovaných s [PDU](/mobilnisite/slovnik/pdu/) Session nebo konkrétní Service Data Flow ([SDF](/mobilnisite/slovnik/sdf/)), akumulaci počtu bajtů v rámci trvání okna a výpočet průměrné rychlosti pro porovnání s předdefinovanými prahovými hodnotami politik, jako jsou ty v Usage Monitoring Control nebo v pravidlech QoS politik.

Architektonicky je AW klíčovou součástí sady pravidel PCC, kterou PCF poskytuje Session Management Function ([SMF](/mobilnisite/slovnik/smf/)). SMF pak tato pravidla vynucuje odpovídající konfigurací UPF. Když UPF provádí detekci a měření provozu, aplikuje AW ke zprůměrování okamžité datové rychlosti. Například pokud je pro tok se zaručenou přenosovou rychlostí ([GBR](/mobilnisite/slovnik/gbr/)) nakonfigurováno AW o délce 60 sekund, UPF vypočítá průměrnou datovou rychlost za posledních 60 sekund, aby zjistil, zda tok plní svůj GBR závazek, nebo zda jsou potřebné akce při přetížení. Tím se zabrání přehnaným reakcím sítě na velmi krátkodobé záblesky, které jsou v paketově přepínaném provozu normální.

Role AW zasahuje do více funkcí PCC, včetně monitorování využití pro politiky spravedlivého využití, dynamického vynucování politik pro aplikací řízené tvarování provozu a ověřování QoS. Je nedílnou součástí schopnosti 5G sítě poskytovat konzistentní kvalitu služeb, implementovat vrstvené služební plány a inteligentně řídit síťové přetížení. Oddělením rozhodnutí politik od okamžitých výkyvů AW zvyšuje stabilitu sítě, zlepšuje předvídatelnost uživatelského zážitku a umožňuje sofistikovanější, časově uvědomělé modely účtování. Jeho konfigurace je vysoce flexibilní, což síťovým operátorům umožňuje přizpůsobit citlivost svých řídicích systémů různým službám – od aplikací s nízkou latencí vyžadujících kratší okna až po služby na pozadí, kde je vhodnější delší průměrování.

## K čemu slouží

Průměrovací okno (AW) bylo zavedeno, aby odstranilo omezení okamžitého nebo velmi krátkodobého měření při vynucování politik, které mohlo vést k nepředvídatelnému chování sítě a špatnému uživatelskému zážitku. V systémech před 5G mohly aktivační události politik založené na okamžité datové rychlosti způsobovat zbytečné omezování přenosové rychlosti, nové žádosti o autorizaci nebo účtovací události během běžných záblesků provozu, jako když uživatel otevře webovou stránku nebo spustí video stream. Tato 'nestabilita' v aplikaci politik byla neefektivní a mohla zhoršit vnímanou kvalitu služby. AW poskytuje mechanismus vyhlazení, který zajišťuje, že rozhodnutí politik odrážejí setrvalé vzorce využití spíše než přechodné špičky.

Historicky, jak se sítě vyvíjely směrem k detailnější a dynamičtější kontrole QoS s příchodem 5G a síťového segmentování, se potřeba stabilního a předvídatelného vynucování politik stala klíčovou. AW umožňuje 5G core síti implementovat sofistikované smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) a účtovací modely založené na průměrném výkonu v čase, což lépe odpovídá uživatelskému zážitku a komerčním nabídkám. Řeší problém přehnaných reakcí sítě a umožňuje spolehlivější správu přetížení, spravedlivé sdílení prostředků mezi uživateli a přesné monitorování využití pro účely účtování. Začleněním AW do architektury PCC poskytlo 3GPP operátorům zásadní nástroj pro implementaci inteligentních, časově uvědomělých síťových politik, které vyvažují citlivost se stabilitou.

## Klíčové vlastnosti

- Časové posuvné okno pro průměrování síťového provozu
- Konfigurovatelná délka trvání (např. v sekundách) na pravidlo politiky
- Aplikováno na měření datové rychlosti v uplinku a downlinku
- Nedílná součást Usage Monitoring Control pro politiky spravedlivého využití
- Používáno při vynucování QoS politik k ověření dodržování GBR/NGBR
- Zabraňuje aktivaci politik z přechodných záblesků provozu

## Související pojmy

- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping

---

📖 **Anglický originál a plná specifikace:** [AW na 3GPP Explorer](https://3gpp-explorer.com/glossary/aw/)
