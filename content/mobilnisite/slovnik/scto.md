---
slug: "scto"
url: "/mobilnisite/slovnik/scto/"
type: "slovnik"
title: "SCTO – Soft Combining Timing Offset"
date: 2025-01-01
abbr: "SCTO"
fullName: "Soft Combining Timing Offset"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/scto/"
summary: "SCTO je parametr v MBMS, který spravuje časové rozdíly pro měkké kombinování (soft combining) vysílacích signálů z více buněk. Zajišťuje, že uživatelské zařízení (UE) může správně zarovnat a zkombinov"
---

SCTO je parametr v MBMS, který spravuje časové rozdíly, aby umožnil uživatelskému zařízení (UE) správně zarovnat a zkombinovat identické vysílací signály přijaté z více buněk.

## Popis

Soft Combining Timing Offset (SCTO, časový posun pro měkké kombinování) je klíčový parametr definovaný v rámci architektury služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) v sítích UMTS (3G), specifikovaný v TS 25.331 (protokol [RRC](/mobilnisite/slovnik/rrc/)). Funguje na vrstvě Radio Resource Control (RRC) za účelem usnadnění příjmu s makro-diverzitou, konkrétně měkkého kombinování (soft combining), pro MBMS vysílací přenosy. Měkké kombinování je technika, při které UE přijímá stejná zakódovaná vysílací data z více Node B (základnových stanic) a kombinuje je na úrovni symbolu nebo čipu před dekódováním, aby zlepšila poměr signálu k šumu a potlačila útlum.

Parametr SCTO poskytuje UE informaci o relativních časových rozdílech mezi přenosy stejného MBMS obsahu z různých buněk v rámci oblasti Multicast/Broadcast Single Frequency Network ([MBSFN](/mobilnisite/slovnik/mbsfn/)) nebo pro scénáře selektivního kombinování. Síť vypočítá maximální očekávaný časový posun mezi libovolnými dvěma buňkami, které může UE přijímat, a tuto hodnotu signalizuje prostřednictvím System Information Block 5 (SIB5) nebo prostřednictvím zprávy MBMS MODIFIED SERVICES INFORMATION na logickém kanálu [MCCH](/mobilnisite/slovnik/mcch/). UE používá tento posun ke konfiguraci časového okna svého přijímače, čímž zajišťuje, že může signály z různých zdrojů před procesem kombinování uložit do vyrovnávací paměti a časově zarovnat.

Z architektonického hlediska SCTO spravuje Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) v [UTRAN](/mobilnisite/slovnik/utran/), který zná časování přenosu všech zúčastněných Node B pro danou MBMS službu. RNC určuje hodnotu SCTO na základě přesnosti synchronizace Node B a geografické velikosti oblasti MBMS služby. Klíčovými zapojenými komponentami jsou RNC (signalizační entita), Node B (přenosové body) a fyzická vrstva a vrstva [MAC](/mobilnisite/slovnik/mac/) v UE, které provádějí vlastní měkké kombinování s využitím poskytnutých časových informací.

Jeho úlohou je maximalizovat zisk z diverzity a pokrytí služeb MBMS vysílání bez nutnosti dokonale synchronizovaných přenosů ze všech buněk, což by v rozsáhlých sítích bylo nepraktické. Tím, že síť informuje UE o povoleném časovém posunu, umožňuje řízenou míru variace v časování přenosu, což zjednodušuje požadavky na plánování sítě a synchronizaci, a přitom stále umožňuje UE provádět efektivní kombinování. To vede k lepší kvalitě služby, zejména na okrajích buněk.

## K čemu slouží

SCTO bylo vytvořeno, aby vyřešilo praktické výzvy implementace měkkého kombinování pro [MBMS](/mobilnisite/slovnik/mbms/) v asynchronních nebo kvazi-synchronních sítích UMTS. Před MBMS bylo měkké předávání (soft handover) pro jednosměrný (unicast) provoz přísně řízeno RNC s přesnými časovými úpravami (jako procedura Timing Advance). Pro bodově-vícebodové (point-to-multipoint) vysílání však takové přísné řízení na úrovni jednotlivých UE není proveditelné. Problémem bylo, jak umožnit UE těžit ze zisku makro-diverzity z více buněk, aniž by bylo nutné, aby všechny buňky byly dokonale synchronizovány na úrovni rámců, což je nákladné a složité.

Řeší omezení spočívající v požadavku na ideální synchronizaci v široké oblasti. Signalizací povoleného časového posunu síť poskytuje UE potřebné informace pro vhodnou konfiguraci vyrovnávacích pamětí přijímače. To bylo motivováno potřebou učinit MBMS ekonomicky životaschopným, neboť umožnilo operátorům nasazovat vysílací služby s využitím stávajících, nedokonale synchronizovaných, míst buněk, a přitom dosáhnout významného zlepšení výkonu oproti příjmu z jedné buňky, což zlepšuje pokrytí a snižuje potřebný vysílací výkon.

## Klíčové vlastnosti

- Umožňuje měkké kombinování (soft combining) MBMS přenosů z více buněk
- Parametr signalizovaný prostřednictvím RRC, který informuje UE o maximálním časovém rozdílu
- Umožňuje kvazi-synchronní provoz sítě, čímž uvolňuje požadavky na synchronizaci
- Zlepšuje pokrytí a spolehlivost vysílání, zejména na okrajích buněk
- Spravován RNC na základě topologie sítě a přesnosti synchronizace
- Klíčový pro příjem s makro-diverzitou pro MBMS v sítích UTRA

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)

## Definující specifikace

- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SCTO na 3GPP Explorer](https://3gpp-explorer.com/glossary/scto/)
