---
slug: "prs-epre-max"
url: "/mobilnisite/slovnik/prs-epre-max/"
type: "slovnik"
title: "PRS-EPRE-MAX – Maximum downlink RS-EPRE"
date: 2025-01-01
abbr: "PRS-EPRE-MAX"
fullName: "Maximum downlink RS-EPRE"
category: "Physical Layer"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/prs-epre-max/"
summary: "Parametr definující maximální povolenou energii na zdrojový prvek (Energy Per Resource Element) pro downlinkové referenční signály, včetně PRS. Nastavuje horní limit, o kolik může základnová stanice z"
---

PRS-EPRE-MAX je maximální povolená energie referenčního signálu na zdrojový prvek (resource element) v downlinku, která nastavuje horní limit výkonu pro polohovací signály, aby se zajistila přesná měření a zároveň byla řízena interference.

## Popis

PRS-EPRE-MAX je klíčový parametr pro řízení výkonu ve specifikacích 3GPP, který definuje maximální přípustnou energii na zdrojový prvek (Energy Per Resource Element, [EPRE](/mobilnisite/slovnik/epre/)) pro downlinkové referenční signály, přičemž má zvláštní význam pro polohovací referenční signály (Positioning Reference Signals, [PRS](/mobilnisite/slovnik/prs/)). EPRE představuje vysílanou energii přidělenou jednomu zdrojovému prvku (jedné podnosné v rámci jednoho [OFDM](/mobilnisite/slovnik/ofdm/) symbolu) v downlinkové fyzické zdrojové mřížce. U PRS může síť záměrně zvýšit jeho EPRE vzhledem k EPRE zdrojových prvků nesoucích data ([PDSCH](/mobilnisite/slovnik/pdsch/)), aby se zlepšil poměr signálu k šumu a interferenci ([SINR](/mobilnisite/slovnik/sinr/)) na přijímači UE, což je zásadní pro přesná měření času příchodu. Parametr PRS-EPRE-MAX nastavuje absolutní horní hranici tohoto zvýšení, vyjádřenou v dB vzhledem k referenční úrovni výkonu (často nominální EPRE PDSCH). Tento limit je vysílán v systémových informacích nebo poskytován prostřednictvím vyhrazené signalizace [RRC](/mobilnisite/slovnik/rrc/) jako součást konfigurace PRS, čímž se zajistí, že všechny UE v buňce znají maximální očekávanou úroveň výkonu, což napomáhá přijímacím algoritmům, jako je automatické řízení zesílení a potlačení interference.

Z architektonického hlediska je PRS-EPRE-MAX spravován funkcemi řízení rádiových zdrojů (Radio Resource Management, [RRM](/mobilnisite/slovnik/rrm/)) uvnitř základnové stanice (eNodeB nebo gNB). Plánovač a výkonový zesilovač základnové stanice se musí tohoto maximálního limitu držet při přidělování výkonu různým downlinkovým kanálům. Skutečně vysílané EPRE PRS může být dynamicky upravováno pod tímto maximem na základě faktorů, jako je zatížení buňky, podmínky interference a požadavky na přesnost polohování. Parametr je definován na nosnou a může být konfigurován odlišně pro různé frekvenční vrstvy nebo části šířky pásma ve scénářích agregace nosných. V kontextu polohování umožňuje vyšší hodnota PRS-EPRE-MAX síti vysílat PRS s větším výkonem, díky čemuž jsou signály detekovatelné na delší vzdálenosti a v hlučném prostředí, což přímo zlepšuje slyšitelnost sousedních buněk pro [OTDOA](/mobilnisite/slovnik/otdoa/). Zvyšování výkonu PRS však také zvyšuje interferenci do jiných buněk a spotřebovává rezervu výkonového zesilovače, která by mohla být využita pro přenos dat; PRS-EPRE-MAX tedy představuje pečlivě zvolený kompromis.

Jak to funguje, zahrnuje jak konfiguraci sítě, tak postupy měření na UE. Operátor sítě nakonfiguruje hodnotu PRS-EPRE-MAX na základě strategie nasazení – např. hustá městská mikrobunka může používat nižší hodnotu pro omezení interference, zatímco venkovská makrobunka může používat vyšší hodnotu pro rozšíření pokrytí PRS. Tato hodnota je sdělena UE. Když UE provádí měření PRS, využívá znalost PRS-EPRE-MAX pro škálování očekávání svého přijímače a pro přesný odhad útlumu na dráze a času příchodu. Pro testování shody se PRS-EPRE-MAX používá k definování testovacích podmínek pro výkon polohování UE, jak je specifikováno v 3GPP TS 37.544 (LTE) a TS 38.151 (NR). UE musí prokázat schopnost dosáhnout specifikované přesnosti měření RSTD, když je přijímaný výkon PRS na úrovních definovaných vzhledem k tomuto maximu. Tím je zajištěna interoperabilita a konzistentní výkon polohování napříč různými implementacemi UE a nasazeními sítí.

## K čemu slouží

PRS-EPRE-MAX byl zaveden za účelem standardizace a řízení zvýšení výkonu polohovacích referenčních signálů, což se stalo nezbytným s rostoucími požadavky na přesnost polohování. V raných verzích LTE nebylo přidělování výkonu pro PRS explicitně omezeno, což vedlo k potenciálním problémům s interoperabilitou a nekontrolované mezi-buněčné interferenci. Bez definovaného maxima mohl jeden operátor nadměrně zvýšit výkon PRS, aby zlepšil vlastní polohovací službu, ale to mohlo způsobit významnou interferenci do sousedních buněk stejného nebo jiného operátora a zhoršit celkový výkon sítě. Tento parametr byl vytvořen, aby poskytl řízený mechanismus pro zlepšení slyšitelnosti PRS při zachování stability sítě.

Tento parametr řeší problém vyvážení výkonu polohování s efektivitou sítě. Nastavením sítí definovaného maxima mohou operátoři zajistit, že zvýšení výkonu PRS je dostatečné pro splnění regulatorních a servisních cílů přesnosti (např. pro E911), aniž by způsobovalo škodlivou interferenci. Také umožňuje předvídatelné chování přijímače UE; UE mohou být navrženy s předpokladem známé maximální vstupní úrovně výkonu pro PRS, což zjednodušuje návrh vstupního stupně a měřicí algoritmy. Při testování a certifikaci poskytuje PRS-EPRE-MAX referenční bod pro definování nejhorších a typických testovacích scénářů, čímž se zajišťuje, že UE splňují minimální výkonnostní standardy za specifikovaných podmínek výkonu.

Historicky se potřeba takového parametru ukázala zřejmou s komercializací polohování v LTE a zavedením funkcí, jako je vylepšený OTDOA ve verzi 14, který cílil na přesnost pod 50 metrů. Jak sítě nasazovaly více malých buněk a heterogenní sítě, řízení interference se stalo složitějším. PRS-EPRE-MAX spolu s dalšími parametry řízení výkonu umožnil koordinované nastavení výkonu napříč buňkami, což je obzvláště důležité pro vzory utlumování PRS a konfigurace téměř prázdných podrámců (almost blank subframe, ABS). Jeho zařazení do specifikací shody (od verze 14 dále) zajistilo, že výkon polohování UE může být spolehlivě ověřen, což operátorům dává jistotu při nasazování služeb založených na poloze. PRS-EPRE-MAX je tedy klíčovým prvkem pro robustní polohování s vysokou přesností v moderních 4G a 5G sítích.

## Klíčové vlastnosti

- Definuje horní limit energie na zdrojový prvek (Energy Per Resource Element, EPRE) pro downlinkové referenční signály, konkrétně PRS.
- Konfigurovatelné na buňku a na nosnou, což umožňuje optimalizaci výkonu polohovacích signálů specifickou pro dané nasazení.
- Umožňuje zvýšení výkonu PRS pro zlepšení SINR a slyšitelnosti pro měření OTDOA při současném řízení interference.
- Vysíláno v systémových informacích nebo poskytováno prostřednictvím signalizace RRC jako součást pomocných dat konfigurace PRS.
- Používá se jako referenční bod pro testování shody UE z hlediska výkonu polohování (např. v TS 37.544).
- Integruje se s celkovým přidělováním výkonu v downlinku a strategiemi RRM pro vyvážení kvality polohovacích a datových služeb.

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TS 38.151** (Rel-19) — NR UE MIMO OTA Performance Requirements
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance

---

📖 **Anglický originál a plná specifikace:** [PRS-EPRE-MAX na 3GPP Explorer](https://3gpp-explorer.com/glossary/prs-epre-max/)
