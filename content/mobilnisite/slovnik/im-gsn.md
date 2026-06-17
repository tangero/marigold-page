---
slug: "im-gsn"
url: "/mobilnisite/slovnik/im-gsn/"
type: "slovnik"
title: "IM-GSN – Intermediate GSN"
date: 2025-01-01
abbr: "IM-GSN"
fullName: "Intermediate GSN"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/im-gsn/"
summary: "Intermediate GSN (IM-GSN) je uzel podpory GPRS, který v roamingu funguje jako zprostředkovatel pro uživatelskou rovinu mezi GGSN a SGSN. Umožňuje optimalizované směrování a účtování mezi operátory pro"
---

IM-GSN je uzel podpory GPRS, který v roamingu funguje jako zprostředkovatel pro uživatelskou rovinu mezi GGSN a SGSN, aby umožnil optimalizované směrování a účtování mezi operátory.

## Popis

Intermediate [GSN](/mobilnisite/slovnik/gsn/) (IM-GSN) je funkční role definovaná v architektuře jádra sítě [GPRS](/mobilnisite/slovnik/gprs/) podle 3GPP, konkrétně pro zpracování roamingu mezi různými PLMN (Public Land Mobile Network). Nejde o samostatný fyzický uzel, ale o logickou funkci, kterou lze implementovat v rámci Gateway GPRS Support Node (GGSN) nebo v dedikovaném uzlu. Když mobilní účastník přejde do navštívené sítě, jeho paketové datové relace jsou ukotveny v GGSN jeho domovské sítě (H-GGSN). IM-GSN se nachází v navštívené síti a stojí na cestě uživatelské roviny mezi navštíveným Serving GPRS Support Node (V-SGSN) a H-GGSN. Jeho hlavní funkcí je správa a směrování tunelů [GTP](/mobilnisite/slovnik/gtp/) (GPRS Tunnelling Protocol) pro datový provoz účastníka.

Operačně během aktivace kontextu PDP (Packet Data Protocol) pro roamujícího účastníka V-SGSN naváže GTP tunel s IM-GSN v navštívené síti a IM-GSN následně naváže další GTP tunel s H-GGSN v domovské síti. Veškeré pakety uživatelské roviny procházejí přes IM-GSN. To umožňuje IM-GSN vykonávat několik klíčových funkcí: může uplatňovat politiky místního průniku (pokud jsou podporovány), generovat záznamy o účtování ([CDR](/mobilnisite/slovnik/cdr/)) pro fakturaci operátora navštívené sítě a vynucovat politiky kvality služeb (QoS) podle meziodběratelských roamingových dohod. IM-GSN používá protokol [GTP-C](/mobilnisite/slovnik/gtp-c/) (řídicí) ke správě tunelů a protokol [GTP-U](/mobilnisite/slovnik/gtp-u/) (uživatelský) k přeposílání skutečných IP paketů.

Architektonicky hraje IM-GSN klíčovou roli při oddělení odpovědností za řízení a účtování mezi domovským a navštíveným operátorem. H-GGSN si zachovává celkovou kontrolu nad kontextem PDP a politikami specifickými pro účastníka, zatímco IM-GSN z pohledu navštívené sítě zajišťuje místní směrování a přístup k externí paketové datové síti (např. internetu). Tento model podporuje přesné zúčtování mezi operátory, protože navštívená síť může účtovat za využití rádiových a jádrových síťových zdrojů, zatímco domovská síť účtuje za celkovou službu. Funkce IM-GSN je definována tak, aby zajistila škálovatelný a efektivní roaming pro paketově spínané služby, což je základním kamenem globální mobilní datové konektivity.

## K čemu slouží

IM-GSN byl vytvořen k řešení složitostí účtování a směrování provozu v roamingu [GPRS](/mobilnisite/slovnik/gprs/)/UMTS. V raných architekturách GPRS byl možný jednoduchý model, kde se V-SGSN připojoval přímo k H-GGSN, ale to představovalo pro operátora navštívené sítě značné výzvy. Navštívený operátor měl omezenou viditelnost a kontrolu nad datovým provozem procházejícím jeho sítí, což ztěžovalo přesné měření využití zdrojů pro fakturaci a zúčtování s domovským operátorem.

Hlavním problémem, který IM-GSN řeší, je umožnění spravedlivého a transparentního účtování mezi operátory za roamingové datové služby. Zavedením IM-GSN v navštívené síti může tento operátor generovat vlastní záznamy o účtování ([CDR](/mobilnisite/slovnik/cdr/)) na základě skutečného objemu dat a doby trvání relace zpracované lokálně. To poskytuje jasný základ pro finanční zúčtování mezi operátory. Dále umožňuje navštívené síti uplatňovat na provoz roamujícího účastníka vlastní místní politiky, jako je tvarování provozu nebo zákonné odposlechy, aniž by bylo nutné měnit domovský GGSN.

Historicky bylo jeho specifikace ve verzi Release 99 motivováno komerčním zavedením GPRS a očekáváním rozšířeného datového roamingu. Řešila omezení původního, jednoduššího roamingového modelu, kterému chyběl definovaný bod pro účtování a kontrolu ze strany navštívené sítě. Koncept IM-GSN poskytl potřebný architektonický prvek pro komerční roamingové dohody a zajistil, že operátoři mají technické prostředky k vzájemnému účtování přeneseného provozu, což bylo klíčové pro obchodní model mezinárodních mobilních dat. Také položil základ pro pokročilejší optimalizace roamingu v pozdějších vydáních.

## Klíčové vlastnosti

- Funguje jako zprostředkovatel GTP tunelu mezi V-SGSN a H-GGSN pro roamující uživatele
- Umožňuje generování záznamů o účtování (CDR) navštívené sítě pro zúčtování mezi operátory
- Poskytuje bod pro uplatňování politik kvality služeb (QoS) a správy provozu navštívené sítě
- Podporuje logické oddělení odpovědností za řízení (domovská síť) a uživatelskou rovinu (navštívená síť)
- Může být implementován jako funkční podmnožina v rámci GGSN nebo jako samostatný uzel
- Usnadňuje škálovatelnou a spravovatelnou architekturu roamingu GPRS/UMTS

## Související pojmy

- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TS 23.119** (Rel-19) — Gateway Location Register (GLR) Stage 2 Description

---

📖 **Anglický originál a plná specifikace:** [IM-GSN na 3GPP Explorer](https://3gpp-explorer.com/glossary/im-gsn/)
