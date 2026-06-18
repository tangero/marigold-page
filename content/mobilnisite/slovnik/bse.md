---
slug: "bse"
url: "/mobilnisite/slovnik/bse/"
type: "slovnik"
title: "BSE – Base Station Emulator"
date: 2025-01-01
abbr: "BSE"
fullName: "Base Station Emulator"
category: "Radio Access Network"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/bse/"
summary: "Testovací systém, který emuluje chování skutečné základnové stanice (eNodeB/gNB) pro testování uživatelského zařízení (UE) v kontrolovaném laboratorním prostředí. Je klíčový pro testování shody, ověřo"
---

BSE je testovací systém, který emuluje skutečnou základnovou stanici pro testování mobilních zařízení v kontrolovaném laboratorním prostředí za účelem ověření jejich shody a výkonnosti s normami 3GPP.

## Popis

Emulátor základnové stanice (BSE) je sofistikovaná testovací platforma definovaná ve specifikacích 3GPP 37.976 a 37.977. Funguje jako simulovaný uzel rádiové přístupové sítě, který implementuje protokoly a chování sítě na straně eNodeB (pro LTE) nebo gNB (pro 5G NR) pro interakci se skutečným testovaným uživatelským zařízením (UE). BSE poskytuje plně říditelné a opakovatelné [RF](/mobilnisite/slovnik/rf/) prostředí, které umožňuje testovacím inženýrům vystavit UE specifickým signalizačním scénářům, podmínkám datového provozu a zkreslením rádiového kanálu, které by bylo obtížné nebo nemožné spolehlivě reprodukovat v živé síti.

Architektonicky se systém BSE skládá z několika klíčových komponent. Jádrem je emulátor protokolového zásobníku, který implementuje celou sadu protokolů 3GPP vrstvy 2 a 3 ([RRC](/mobilnisite/slovnik/rrc/), [PDCP](/mobilnisite/slovnik/pdcp/), [RLC](/mobilnisite/slovnik/rlc/), [MAC](/mobilnisite/slovnik/mac/)) a řídicích rovin procedur pro rozhraní vzduchu. Ten je těsně integrován s jednotkou pro zpracování základního pásma, která generuje signály fyzické vrstvy (downlink) a zpracovává přijaté signály (uplink) podle specifikované numerologie, tvaru vlny a rámcové struktury. Kritickým subsystémem je RF front-end, který provádí digitálně-analogový/analogově-digitální převod, převod na cílovou kmitočtovou nosnou a poskytuje přesnou regulaci vysílaného výkonu. Systém je řízen testovacím řídicím a ovládacím softwarem, který orchestruje komplexní testovací sekvence, zaznamenává veškerou signalizaci a výměnu dat a poskytuje rozhraní pro testovací automatizaci.

Během provozu BSE naváže a udržuje simulované rádiové spojení s UE. Iniciuje procedury jako vyhledávání a výběr buňky, vysílání systémových informací, náhodný přístup, navázání RRC spojení a zřízení přenosového kanálu. Jakmile je spojení aktivní, může BSE generovat downlinkový uživatelský provoz a přijímat uplinkový provoz z UE, přičemž měří propustnost, latenci a míru chybovosti paketů. Definující schopností je integrace emulátoru útlumu (fading emulator) nebo simulátoru kanálu. Tato komponenta aplikuje přesné matematické modely (např. [TDL](/mobilnisite/slovnik/tdl/), [CDL](/mobilnisite/slovnik/cdl/)) na signály základního pásma, čímž simuluje efekty vícecestného šíření, Dopplerova posuvu a útlumu na dráze, které se vyskytují v reálných mobilních scénářích. To umožňuje testování výkonnosti za řízených podmínek útlumu.

Role BSE v síťovém ekosystému je zásadní pro certifikaci zařízení a zajištění kvality. Je to primární nástroj používaný testovacími laboratořemi (jako jsou laboratoře uznané [GCF](/mobilnisite/slovnik/gcf/) a PTCRB) k provádění standardizovaných testovacích případů shody definovaných 3GPP. Tyto testy ověřují, že UE správně implementuje povinné protokoly a chová se podle specifikace jak za normálních, tak za výjimečných podmínek. Nad rámec testování shody jsou BSE rozsáhle používány výrobci čipových sad a zařízení pro výzkum a vývoj, ladění, regresní testování a optimalizaci výkonnosti během celého životního cyklu vývoje produktu, čímž se zajišťuje robustnost a interoperabilita zařízení ještě před jejich uvedením ke koncovým uživatelům.

## K čemu slouží

BSE byl vytvořen, aby řešil kritickou potřebu důkladného, standardizovaného a opakovatelného testování uživatelského zařízení v laboratorním prostředí. Před formalizací těchto emulovaných testovacích systémů se rané testování zařízení často provádělo v živých sítích operátorů nebo s proprietárními testovacími sestavami. Tento přístup byl nekonzistentní, neopakovatelný, časově náročný a nemohl garantovat komplexní pokrytí složitých stavů protokolů a chybových stavů vyžadovaných normami 3GPP. Nedostatek kontrolovaného prostředí ztěžoval izolaci a ladění problémů zařízení, což vedlo k delším vývojovým cyklům a potenciálním problémům s interoperabilitou při nasazení zařízení od různých dodavatelů v reálných sítích.

Zavedení BSE, zejména s jeho podrobnou specifikací v 3GPP Release 10, poskytlo řešení těchto problémů. Stanovilo společnou referenční platformu, vůči které lze všechna UE testovat, což zajistilo rovné podmínky a konzistentní interpretaci norem. Primární problém, který řeší, je umožnit ověření s vysokou mírou důvěry, že UE je v souladu s technickými specifikacemi 3GPP pro rádiový přenos, příjem, signalizaci a procedury. To je předpoklad pro síťové operátory, kteří požadují certifikaci zařízení (např. prostřednictvím GCF nebo PTCRB), aby zajistili, že zařízení nezpůsobí narušení sítě nebo nezhorší kvalitu služeb pro ostatní uživatele.

Dále BSE umožňuje testovací scénáře, které jsou v živé síti nepraktické nebo nebezpečné, jako je testování odolnosti protokolů vůči chybně formátovaným zprávám, ověřování chování při selhání a obnově rádiového spoje nebo hodnocení výkonnosti na extrémních okrajích pokrytí buňky. Tím, že poskytuje přesnou kontrolu nad každým aspektem simulovaného rádiového rozhraní – od vysílacího výkonu a časování až po podmínky kanálu a síťovou signalizaci – dává BSE inženýrům možnost důkladně ověřit výkonnost a spolehlivost zařízení ještě před sériovou výrobou a komerčním nasazením, což v konečném důsledku zvyšuje kvalitu a stabilitu celého mobilního ekosystému.

## Klíčové vlastnosti

- Plná emulace protokolového zásobníku pro LTE a/nebo 5G NR řídicí a uživatelské roviny
- Přesné generování a analýza RF signálu s kalibrovanou regulací výkonu
- Integrovaná emulace útlumu kanálu pro realistické testování vícecestného šíření a mobility
- Provedení testovacích případů shody definovaných 3GPP (TTCN-3)
- Vysoce přesné časování a synchronizace pro emulaci struktury rámců a slotů
- Komplexní nástroje pro zaznamenávání a analýzu signalizace a metrik výkonnosti

## Definující specifikace

- **TR 37.976** (Rel-19) — MIMO OTA Test Methodology Study
- **TR 37.977** (Rel-19) — MIMO OTA Test Methodology

---

📖 **Anglický originál a plná specifikace:** [BSE na 3GPP Explorer](https://3gpp-explorer.com/glossary/bse/)
