---
slug: "spid"
url: "/mobilnisite/slovnik/spid/"
type: "slovnik"
title: "SPID – Subscriber Profile ID for RAT/Frequency Priority"
date: 2025-01-01
abbr: "SPID"
fullName: "Subscriber Profile ID for RAT/Frequency Priority"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/spid/"
summary: "Identifikátor konfigurovaný sítí, který slouží k přiřazení specifických priorit výběru rádiové přístupové technologie (RAT) a kmitočtu účastníkovi. Umožňuje operátorům nasměrovávat uživatelské zařízen"
---

SPID je identifikátor konfigurovaný sítí, který slouží k přiřazení specifických priorit výběru rádiové přístupové technologie a kmitočtu účastníkovi, což operátorům umožňuje nasměrovávat uživatelské zařízení na preferované sítě.

## Popis

Subscriber Profile ID for [RAT](/mobilnisite/slovnik/rat/)/Frequency Priority (SPID) je klíčový parametr v architektuře 3GPP pro správu výběru sítě a řízení provozu. Jedná se o číselný identifikátor, typicky v rozsahu 1 až 256, uložený v profilu účastníka v databázi Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo podobné. Toto ID není uživateli přímo viditelné, ale síť jej používá k odkazování na konkrétní sadu operátorem definovaných pravidel. Tato pravidla určují pořadí priority, ve kterém by se mělo uživatelské zařízení (UE) pokoušet připojit (camp on) nebo předat spojení (handover) k různým rádiovým přístupovým technologiím (např. LTE, [WCDMA](/mobilnisite/slovnik/wcdma/), GSM) a specifickým kmitočtovým pásmům v rámci těchto technologií.

Když se UE připojí k síti, SPID je načten z HSS a odeslán do Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v Evolved Packet Core (EPC) nebo do funkce Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G Core (5GC). Uzel jádra sítě poté poskytne tento SPID spolu s přidruženým indexem RAT/Frequency Selection Priority ([RFSP](/mobilnisite/slovnik/rfsp/)) do rádiové přístupové sítě (RAN). V 4G je toto sděleno eNodeB přes rozhraní S1; v 5G je odesláno gNodeB přes rozhraní [NG](/mobilnisite/slovnik/ng/). Uzel RAN používá tuto informaci k inteligentnímu rozhodování ohledně převýběru buňky v režimu nečinnosti (idle mode) a předání spojení v režimu připojení (connected mode).

Primární mechanismus spočívá v mapování SPID na index RFSP, což je lokalizovaná tabulka v uzlu RAN. Tato tabulka obsahuje skutečné hodnoty priority pro každou RAT a kmitočtový nosič. Například operátor může nakonfigurovat SPID=10 tak, aby se mapoval na index RFSP, který přiřadí nejvyšší prioritu LTE pásmu 3, střední prioritu LTE pásmu 20 a nejnižší prioritu UMTS. To umožňuje detailní, na předplatné založené řízení provozu. RAN uplatňuje tyto priority, když je UE v režimu nečinnosti, aby ovlivnil výběr buňky, a v režimu připojení, aby ovlivnil rozhodování o předání spojení, čímž zajišťuje, že účastníci jsou směrováni na síťovou vrstvu, která nejlépe odpovídá jejich služebnímu plánu a cílům operátora v distribuci provozu.

## K čemu slouží

SPID byl zaveden, aby vyřešil problém specifického síťového směrování na úrovni účastníka v prostředí s více [RAT](/mobilnisite/slovnik/rat/) a více kmitočty. Před jeho zavedením byl výběr sítě a předání spojení založeno primárně na rádiových měřeních (např. síla signálu) a statických konfiguracích na úrovni buňky, které platily stejně pro všechny uživatele. Tento přístup byl neefektivní pro zvládání přetížení sítě, implementaci diferenciace úrovní služeb (např. prémioví vs. základní účastníci) a optimalizaci využití spektra. Operátoři postrádali dynamický nástroj, který by byl vědomý účastníka, pro směrování provozu.

Vytvoření SPID bylo motivováno potřebou sofistikovanějšího řízení provozu založeného na politikách. Umožňuje operátorům definovat obchodní a technická pravidla na úrovni účastníka a vynucovat je prostřednictvím RAN. Například operátor může použít SPID k zajištění, že prémioví firemní účastníci jsou vždy udržováni na LTE nosičích s nejvyšší kapacitou, zatímco ostatní účastníci mohou být během špičkového přetížení nasměrováni na jiná pásma nebo dokonce na 3G. Také usnadňuje zavádění nových technologií a kmitočtových pásem; operátor může postupně migrovat specifické skupiny uživatelů na novou 5G vrstvu tím, že jim přiřadí SPID s vysokou prioritou pro 5G kmitočty. Tento na účastníka zaměřený přístup je zásadní pro efektivní provoz sítě, diferenciaci kvality služeb a strategické řízení spektra.

## Klíčové vlastnosti

- Přiřazení síťové priority specifické pro účastníka
- Mapování na indexy RAT/Frequency Selection Priority (RFSP)
- Řízení jak převýběru buňky v režimu nečinnosti, tak předání spojení v režimu připojení
- Uložení v HSS/UDM jako součást profilu účastníka
- Signalizace z jádra sítě (MME/AMF) do RAN (eNodeB/gNodeB)
- Umožňuje diferenciaci úrovní služeb a správu přetížení

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)

## Definující specifikace

- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 48.018** (Rel-19) — BSS-SGSN Interface for GPRS Control

---

📖 **Anglický originál a plná specifikace:** [SPID na 3GPP Explorer](https://3gpp-explorer.com/glossary/spid/)
