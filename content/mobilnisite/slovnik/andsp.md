---
slug: "andsp"
url: "/mobilnisite/slovnik/andsp/"
type: "slovnik"
title: "ANDSP – Access Network Discovery and Selection Policy"
date: 2026-01-01
abbr: "ANDSP"
fullName: "Access Network Discovery and Selection Policy"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/andsp/"
summary: "ANDSP je rámec zásad (politiky), který umožňuje UE objevovat a vybírat sítě přístupu mimo 3GPP (např. Wi-Fi) na základě operátorem definovaných pravidel. Poskytuje inteligentní výběr sítě přesahující"
---

ANDSP je rámec zásad (politiky), který umožňuje uživatelskému zařízení objevovat a vybírat sítě přístupu mimo 3GPP (např. Wi-Fi) na základě operátorem definovaných pravidel pro inteligentní výběr sítě.

## Popis

Access Network Discovery and Selection Policy (ANDSP) je komplexní rámec pro správu zásad definovaný v architektuře 5G System (5GS), který řídí, jak User Equipment (UE) objevuje, vyhodnocuje a vybírá sítě přístupu mimo 3GPP, primárně bezdrátové lokální sítě (WLANs/Wi-Fi). Funguje jako klíčová součást konceptu legacy Access Network Discovery and Selection Function ([ANDSF](/mobilnisite/slovnik/andsf/)), který je nyní hlouběji integrován do Policy Control Framework ([PCF](/mobilnisite/slovnik/pcf/)) jádra 5G. Zásada je doručena ze sítě na UE, typicky prostřednictvím signalizace Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) nebo mechanismů uživatelské roviny, a je uložena lokálně v zařízení k provedení.

Z architektonického hlediska jsou politiky ANDSP strukturovány jako sada pravidel a preferencí definovaných v dokumentu Extensible Markup Language ([XML](/mobilnisite/slovnik/xml/)) nebo jiném strukturovaném formátu dat. Rámec zásad obsahuje několik klíčových součástí: Discovery Information, které poskytuje UE údaje o dostupných sítích mimo 3GPP v jeho okolí (jako [SSID](/mobilnisite/slovnik/ssid/), [HESSID](/mobilnisite/slovnik/hessid/) nebo seznamy realm); Selection Criteria, které definuje pravidla a priority pro výběr jedné sítě před druhou; a Validity Conditions, které určují časový a prostorový rozsah, kde je zásada platná. Klient ANDSP v UE interpretuje tyto zásady, často ve spolupráci s operačním systémem zařízení a správcem připojení, aby provedl rozhodnutí o výběru sítě.

Při provozu UE používá ANDSP k činění inteligentních rozhodnutí o výběru přístupu. Pokud je k dispozici více přístupových sítí (např. 5G NR, LTE a Wi-Fi 6), UE konzultuje pravidla ANDSP. Tato pravidla mohou být založena na široké škále faktorů přesahujících jednoduchý Received Signal Strength Indicator ([RSSI](/mobilnisite/slovnik/rssi/)). Patří mezi ně umístění UE (pomocí geografických souřadnic nebo [PLMN](/mobilnisite/slovnik/plmn/)), denní doba, konkrétní používaná aplikace nebo služba (mapovaná pomocí DNN, S-NSSAI nebo OSId/OSAppId), požadované úrovně QoS, podmínky zatížení sítě, preference uživatele a stav roamingu. Například zásada může stanovit, že pro službu streamování videa ve vysokém rozlišení (identifikovanou pomocí jejího S-NSSAI) by mělo UE upřednostnit důvěryhodnou Wi-Fi síť s vysokou propustností před mobilním připojením, pokud je dostupná, pokud ovšem mobilní připojení není z domovského PLMN a Wi-Fi není nedůvěryhodný hotspot.

Role ANDSP je klíčová pro umožnění plynulé mobility a kontinuity relací napříč heterogenními přístupovými sítěmi. Je základním prvkem pro funkce Access Traffic Steering, Switching, and Splitting (ATSSS) definované v 3GPP, které umožňují síti směrovat konkrétní IP toky k nejvhodnějšímu přístupu (3GPP nebo non-3GPP). Díky přesunu síťové inteligence na UE prostřednictvím zásad snižuje ANDSP potřebu neustálé síťové signalizace během fází objevování a umožňuje kontextově citlivější, efektivnější a uživatelsky orientovanější správu připojení. Účinně propojuje mechanismy řízení zásad jádra 5G se skutečnými rozhodnutími o připojení přijímanými na hraničním zařízení.

## K čemu slouží

ANDSP byl vytvořen, aby vyřešil kritickou výzvu inteligentního a efektivního výběru přístupové sítě v stále heterogennějších bezdrátových prostředích. Před jeho standardizací bylo chování UE při výběru mezi mobilní a Wi-Fi sítí velmi zjednodušené, často založené pouze na síle signálu nebo ručním zásahu uživatele. To vedlo k neoptimálnímu využití sítě, špatnému uživatelskému zážitku (např. když se UE drželo slabého, ale preferovaného mobilního signálu namísto přepnutí na silnou Wi-Fi) a neschopnosti operátorů strategicky spravovat provoz napříč svým portfoliem více typů přístupu. Rozšíření Wi-Fi jako klíčového doplňku k mobilním sítím, zejména pro odlehčování datového provozu a pokrytí v interiérech, si vyžádalo standardizovaný, zásadami řízený přístup.

Tato technologie řeší omezení dřívějších, nestandardizovaných metod tím, že poskytuje jednotný, operátorem řízený rámec. Umožňuje Mobile Network Operators (MNOs) definovat sofistikovaná obchodní a technická pravidla pro výběr přístupu, která jsou pak vynucována na UE. To řeší problémy, jako je nekontrolované odlehčování, které může zatížit určité Wi-Fi sítě, neschopnost upřednostnit přístup pro konkrétní služby (jako je hlas přes Wi-Fi) a špatná podpora plynulé mobility mezi typy přístupu. Historicky koncept vznikl s ANDSF ve 3GPP Release 8 pro EPS, ale ANDSP v 5G představuje evoluci, která nabízí těsnější integraci s architekturou 5G jádra založenou na službách a detailnější řízení zásad v souladu s network slicing a QoS toky.

Dále je ANDSP motivován potřebou podporovat komplexní případy užití 5G. Pro enhanced Mobile Broadband (eMBB) zajišťuje, že uživatelé jsou vždy připojeni k nejlepšímu dostupnému přístupu pro aplikace s vysokou propustností. Pro network slicing může obsahovat pravidla výběru specifická pro slice, což zajišťuje, že se UE připojí k přístupové síti schopné podporovat požadovaný slice. Pro ATSSS poskytuje základní zásady, které určují, jak je provoz směrován nebo rozdělován. V konečném důsledku ANDSP umožňuje operátorům optimalizovat jejich celkové síťové zdroje, zlepšit zákaznický zážitek a implementovat pokročilé strategie správy provozu ve světě 5G s více typy přístupu.

## Klíčové vlastnosti

- Poskytování operátorem definovaných zásad na UE prostřednictvím standardizovaných rozhraní
- Výběr sítě založený na pravidlech s kritérii jako umístění, čas, typ služby (DNN/S-NSSAI) a stav roamingu
- Podpora pro poskytování informací o objevování (např. seznamy preferovaných SSID, seznamy realm)
- Umožňuje funkci Access Traffic Steering, Switching, and Splitting (ATSSS)
- Těsná integrace s Policy Control Framework (PCF) 5G pro dynamické aktualizace
- Zlepšuje plynulou mobilitu a kontinuitu relací napříč přístupy 3GPP a non-3GPP

## Definující specifikace

- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TR 26.941** (Rel-19) — 5G Media Slicing Extensions
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3

---

📖 **Anglický originál a plná specifikace:** [ANDSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/andsp/)
