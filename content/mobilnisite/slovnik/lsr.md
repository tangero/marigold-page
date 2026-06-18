---
slug: "lsr"
url: "/mobilnisite/slovnik/lsr/"
type: "slovnik"
title: "LSR – Late Stage Reprojection"
date: 2025-01-01
abbr: "LSR"
fullName: "Late Stage Reprojection"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lsr/"
summary: "Vykreslovací technika používaná v aplikacích rozšířené reality (XR) přes systémy 5G ke kompenzaci latence mezi pohybem a zobrazením. Upravuje finální obrazový snímek těsně před zobrazením na základě n"
---

LSR je vykreslovací technika pro XR přes 5G, která upravuje finální obrazový snímek pomocí nejnovější polohy zařízení, aby kompenzovala latenci a zlepšila vizuální stabilitu.

## Popis

Late Stage Reprojection (LSR) je pokročilá technika vykreslování a zpracování obrazu definovaná v rámci 3GPP pro podporu služeb rozšířené reality ([XR](/mobilnisite/slovnik/xr/)) přes sítě 5G. Konkrétně řeší problém latence mezi pohybem a zobrazením – zpoždění mezi pohybem uživatele (např. otočením hlavy ve [VR](/mobilnisite/slovnik/vr/)) a odpovídající aktualizací obrazu na displeji. Ve scénáři XR vykreslovaného v cloudu/na edge, kde se složitá 3D grafika vykresluje na vzdáleném serveru a streamuje jako video do lehkého headsetu, může tato latence způsobovat dezorientaci, nevolnost a narušovat pocit ponoření. LSR funguje jako finální korekční krok na klientském zařízení (terminálu XR).

Architektura zahrnuje rozdělené vykreslování. Aplikační server, potenciálně umístěný na síťovém edge, vykreslí primární scénu XR na základě výchozí polohy (pozice a orientace) uživatelova zařízení přijaté přes síť 5G. Tento vykreslený snímek je zakódován a přenesen do zařízení. Během doby přenosu a dekódování se poloha uživatele mírně změní. Namísto zahození snímku nebo čekání na zcela nový snímek ze serveru vezme modul LSR na klientském zařízení dekódovaný snímek a aplikuje na něj geometrickou transformaci (reprojekci). Tato transformace je vypočtena pomocí nejnovějších vysokofrekvenčních dat o poloze z vestavěných senzorů zařízení (gyroskopů, akcelerometrů). Reprojekce typicky zahrnuje deformaci nebo posun obrazových pixelů, aby se virtuální scéna zarovnala s novým úhlem pohledu uživatele.

Jak to funguje technicky: Klientské zařízení udržuje pipeline pro predikci polohy. Když ze sítě dorazí nový videosnímek, klient porovná časovou známku polohy použitou serverem pro vykreslování se svou aktuální, aktualizovanou polohou. Algoritmus LSR následně vypočte potřebnou transformaci (rotaci a někdy i translaci) pro opravu obrazu. Často se jedná o 3D rotační reprojekci, která je méně výpočetně náročná než kompletní převykreslování, ale účinná pro kompenzaci malých rychlých pohybů hlavy. Reprojektovaný snímek je poté odeslán na displej. Tento proces probíhá v posledních milisekundách před obnovením obrazovky, odtud termín 'late stage'. Jeho role je klíčová pro udržení přesvědčivé iluze stabilního virtuálního světa a maskování inherentní latence bezdrátového přenosu a pipeline vzdáleného vykreslování, což je klíčový ukazatel výkonu pro kvalitu uživatelského zážitku u bezdrátového XR.

## K čemu slouží

Late Stage Reprojection byl standardizován v 3GPP, aby vyřešil základní problém latence, který ohrožuje uskutečnitelnost bezdrátové, cloudové rozšířené reality. Kvalitní [XR](/mobilnisite/slovnik/xr/) vyžaduje obrovský výpočetní výkon pro vykreslování, který je ideálně přesunut na výkonné edge servery. Doba oběhu pro odeslání dat o poloze na server, vykreslení snímku a jeho streamování zpět však může snadno překročit práh 20 ms, za nímž se latence stává vnímatelnou a způsobuje simulátorovou nevolnost. Tradiční streamování videa nemá mechanismus pro nápravu tohoto stavu.

LSR existuje, aby oddělil latenci vykreslování od vnímané latence mezi pohybem a zobrazením. Řeší omezení pouhého pokusu o zrychlení sítě; i s ultra-spolehlivou komunikací s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) je určitá latence nevyhnutelná. LSR poskytuje softwarový korekční mechanismus, který funguje v poslední fázi řetězce zobrazení. Byl motivován potřebou umožnit kvalitní, bezdrátové zážitky XR přes sítě 5G, což činí headset lehčí, levnější a mobilnější díky využití síťových výpočetních zdrojů.

Historicky byly podobné techniky používány v samostatných [VR](/mobilnisite/slovnik/vr/) headsetech. Práce 3GPP v Rel-13 a dále formalizovala její požadavky a integraci do architektury systému 5G pro streamování médií, což zajišťuje, že síť (např. prostřednictvím parametrů kvality služby) a aplikační server mohou efektivně spolupracovat s LSR schopností klienta. Řeší problém vizuálního trhání a nestability ve scénách vykreslovaných v cloudu, což je zásadní pro to, aby se profesionální, spotřebitelské a průmyslové aplikace XR staly mainstreamovými přes mobilní připojení.

## Klíčové vlastnosti

- Kompenzuje latenci mezi pohybem a zobrazením v cloudem vykreslovaných XR streamech.
- Provádí geometrickou deformaci obrazu na klientském zařízení pomocí nejnovějších lokálních senzorových dat.
- Funguje ve finální fázi display pipeline těsně před scan-out.
- Snižuje vnímanou latenci bez nutnosti nižší síťové latence.
- Umožňuje použití lehčích, méně výkonných XR terminálů přesunutím náročného vykreslování.
- Definováno ve specifikacích 3GPP pro interoperabilní XR přes systémy 5G.

## Definující specifikace

- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 32.855** (Rel-14) — Study on OAM Support for Licensed Shared Access

---

📖 **Anglický originál a plná specifikace:** [LSR na 3GPP Explorer](https://3gpp-explorer.com/glossary/lsr/)
