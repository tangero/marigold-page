---
slug: "gpon"
url: "/mobilnisite/slovnik/gpon/"
type: "slovnik"
title: "GPON – Gigabit-capable Passive Optical Network"
date: 2025-01-01
abbr: "GPON"
fullName: "Gigabit-capable Passive Optical Network"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gpon/"
summary: "Gigabit-capable Passive Optical Network (GPON) je optická telekomunikační technologie pro širokopásmový přístup, standardizovaná ITU-T a referencovaná v 3GPP pro konvergenci pevných a mobilních sítí."
---

GPON je technologie širokopásmového přístupu po optických vláknech, standardizovaná ITU-T a referencovaná v 3GPP, která poskytuje vysokorychlostní data, hlas a video přes síť typu point-to-multipoint využívající pasivní rozdělovače.

## Popis

Gigabit-capable Passive Optical Network (GPON) je přístupová síťová technologie definovaná v sérii [ITU-T](/mobilnisite/slovnik/itu-t/) G.984. Přestože se nejedná o rádiovou technologii definovanou 3GPP, je referencována ve specifikacích 3GPP (např. TS 24.229 pro IMS, TS 26.942 pro přenos médií) v kontextu konvergence pevných a mobilních sítí ([FMC](/mobilnisite/slovnik/fmc/)) a jako možnost vysokokapacitního transportu pro síťové uzly, včetně scénářů pro přenosovou síť 5G (backhaul) a pevný bezdrátový přístup. GPON je technologie optického vlákna až k účastníkovi (FTTP), která využívá topologii point-to-multipoint (P2MP). Síť se skládá z optické linkové terminace (OLT) v centrále poskytovatele služeb, pasivní optické distribuční sítě (zahrnující vlákna a rozdělovače) a více optických síťových jednotek (ONU) neboli optických síťových terminálů (ONT) v prostorách zákazníka.

Technologie funguje pomocí vlnového multiplexu (WDM), typicky využívá vlnovou délku 1490 nm pro datový tok směrem k účastníkovi (downstream) a 1310 nm pro tok od účastníka (upstream). Provoz směrem k účastníkovi z OLT je vysílán všem ONU, přičemž každá ONU filtruje rámce na základě svého jedinečného identifikátoru. Přenos směrem od účastníka je řízen pomocí vícečetného přístupu s časovým dělením (TDMA), kdy OLT přiděluje každé ONU konkrétní časové sloty pro přenos, aby se zabránilo kolizím na sdíleném vlákně. Toto plánování TDMA je dynamické a umožňuje přizpůsobovat přidělování přenosové kapacity na základě smlouvy o úrovni služeb (SLA) a reálné poptávky každého účastníka.

GPON podporuje asymetrické rychlosti, běžné jsou rychlosti 2,5 Gbps downstream a 1,25 Gbps upstream, ačkoli novější standardy podporují symetrických 10 Gbps (XGS-PON). Nativně přenáší Ethernetové rámce, TDM (časový multiplex) pro zastaralé hlasové služby a rámce GEM (GPON Encapsulation Method) pro efektivní multiplexování různých typů provozu na jedné vlnové délce. Z pohledu 3GPP je GPON významné jako vysokokapacitní a nákladově efektivní řešení pevného přístupu, které lze integrovat s mobilními páteřními sítěmi. Může poskytovat přenosovou síť (backhaul) pro buňkové základnové stanice (např. gNB, [eNB](/mobilnisite/slovnik/enb/)) a sloužit jako přístupová síť pro pevné IMS služby, což umožňuje konvergentní poskytování služeb.

## K čemu slouží

Technologie GPON byla vyvinuta, aby uspokojila exponenciálně rostoucí poptávku po širokopásmové kapacitě pro domácnosti a firmy, poháněnou videostreamingem, cloudovými službami a vysokorychlostním internetem. Řešila omezení předchozích technologií na bázi mědi (jako [DSL](/mobilnisite/slovnik/dsl/)) a aktivních optických sítí, které byly buď kapacitně omezené, nebo nákladné na nasazení a údržbu kvůli aktivním elektronickým komponentám v terénu.

Její účel v ekosystému 3GPP je mnohostranný. Především je uznávána jako klíčová technologie pevného přístupu pro umožnění konvergence pevných a mobilních sítí ([FMC](/mobilnisite/slovnik/fmc/)), což je strategický cíl, kdy jsou služby poskytovány bezproblémově přes pevné i mobilní sítě. GPON poskytuje ultra-vysokorychlostní, nízkolatenční kanál nezbytný pro poskytování služeb založených na IMS (jako VoLTE, ViLTE) do pevných lokalit. Dále, s příchodem 5G a jeho náročnými požadavky na transportní sítě (fronthaul a backhaul), GPON a jeho nástupci (XGS-PON, NG-PON2) nabízejí nákladově efektivní, vysokokapacitní optické řešení pro připojení husté sítě malých buněk a makro stanovišť k páteřní síti, čímž podporují strategie zhušťování sítě.

## Klíčové vlastnosti

- Architektura pasivní optické sítě typu point-to-multipoint využívající rozdělovače
- Vysoká přenosová kapacita (např. 2,5G/1,25G) s dlouhým dosahem (až 20 km)
- Dynamické přidělování přenosové kapacity (DBA) prostřednictvím TDMA pro provoz směrem od účastníka
- Nativní podpora Ethernetu, TDM a GEM enkapsulace
- Robustní provoz a správa prostřednictvím rozhraní OMCI (ONT Management and Control Interface)
- Podpora služeb triple-play (data, hlas, video) přes jedno optické vlákno

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation

---

📖 **Anglický originál a plná specifikace:** [GPON na 3GPP Explorer](https://3gpp-explorer.com/glossary/gpon/)
