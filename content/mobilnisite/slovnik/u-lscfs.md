---
slug: "u-lscfs"
url: "/mobilnisite/slovnik/u-lscfs/"
type: "slovnik"
title: "U-LSCFS – UTRAN Location System Control Function in SAS"
date: 2025-01-01
abbr: "U-LSCFS"
fullName: "UTRAN Location System Control Function in SAS"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/u-lscfs/"
summary: "U-LSCFS je specifická instance U-LSCF navržená pro provoz v architektuře samostatného SMLC (SAS). Poskytuje řídicí funkce pro polohové služby, ale je implementována jako samostatný síťový uzel, nikoli"
---

U-LSCFS je instance funkce řízení polohového systému UTRAN (UTRAN Location System Control Function) v architektuře samostatného SMLC (Standalone SMLC), která poskytuje řízení polohových služeb jako samostatný uzel namísto integrace do RNC.

## Popis

Funkce řízení polohového systému [UTRAN](/mobilnisite/slovnik/utran/) v [SAS](/mobilnisite/slovnik/sas/) (U-LSCFS) je varianta standardní [U-LSCF](/mobilnisite/slovnik/u-lscf/), kde 'SAS' označuje architekturu samostatného [SMLC](/mobilnisite/slovnik/smlc/) (Serving Mobile Location Centre). Zatímco standardní U-LSCF je typicky integrována jako softwarová funkce v radiovém síťovém řadiči ([RNC](/mobilnisite/slovnik/rnc/)), U-LSCFS je implementována jako fyzicky nebo logicky samostatný síťový uzel. Tato samostatná entita vykonává všechny základní řídicí funkce správy polohových služeb, ale činí tak z vyhrazené platformy. Zachovává stejná logická rozhraní a procedury jako jsou definovány pro U-LSCF, primárně rozhraní Iupc ke Core Network a potřebné signalizační spoje k rádiovým uzlům UTRAN (Node B a [LMU](/mobilnisite/slovnik/lmu/)).

Provozně U-LSCFS funguje tak, že přijímá požadavky na polohové služby od [GMLC](/mobilnisite/slovnik/gmlc/) Core Network přes rozhraní Iupc. Po přijetí požadavku zahájí polohovací relaci. Odesílá řídicí příkazy příslušnému RNC nebo přímo Node B (v závislosti na konkrétní implementaci a podpoře rozhraní), aby orchestrovala požadovaná rádiová měření. Pro metody jako [U-TDOA](/mobilnisite/slovnik/u-tdoa/) nebo vylepšený OTDOA také komunikuje se samostatnými jednotkami pro měření polohy (LMU) nasazenými v síti. U-LSCFS shromažďuje hlášení o měřeních, provádí výpočet polohy pomocí příslušného algoritmu a poté vrací vypočtený odhad polohy žádajícímu GMLC. Její samostatná povaha znamená, že může obsluhovat více RNC nebo dokonce pool RNC, čímž centralizuje polohovací inteligenci pro větší oblast sítě.

Architektonické oddělení, které U-LSCFS poskytuje, nabízí významnou flexibilitu nasazení. Umožňuje síťovým operátorům oddělit vývoj polohových služeb od životního cyklu jejich hardwaru RNC. Nové polohovací funkce nebo vylepšení výkonu lze zavést upgradem samostatného uzlu SAS bez nutnosti nákladných a složitých upgradů každého RNC v síti. Tento model také usnadňuje přímočařejší škálování kapacity, protože další uzly SAS lze nasadit nezávisle na infrastruktuře RAN. Dále může zjednodušit správu a provoz sítě vytvořením centralizovaného bodu pro monitorování a řešení problémů všech aktivit polohových služeb v rámci pokrytí UTRAN.

## K čemu slouží

U-LSCFS byla vyvinuta k řešení omezení nasazení a škálovatelnosti spojených s integrovaným modelem U-LSCF. Zatímco integrace řídicí funkce v RNC je efektivní pro těsně propojený systém, může omezovat schopnost operátora rychle nasadit pokročilé polohové služby nebo je škálovat nezávisle na kapacitě RAN. Architektura samostatného SAS, a tedy i U-LSCFS, byla motivována potřebou provozní flexibility a snahou nabízet služby založené na poloze jako modulárnější, potenciálně externalizovanou síťovou schopnost.

Tento přístup řeší problémy spojené se závislostí na dodavateli a heterogenními sítěmi. Operátor s RNC od více dodavatelů by mohl nasadit jediný, na dodavateli nezávislý uzel U-LSCFS, aby poskytoval jednotnou platformu polohových služeb v celé síti. Také zajišťuje budoucí kompatibilitu sítě pro zavedení výpočetně náročnějších polohovacích technik, které mohou být hostovány na vyhrazeném serverovém hardwaru v SAS, namísto spoléhání se na procesní zdroje RNC. Vytvoření U-LSCFS odráží strategický posun k abstrakci na úrovni služeb, což umožňuje, aby se polohové služby vyvíjely jako aplikace oddělená od podkladové technologie rádiového přístupu, což je koncept, který nabývá na důležitosti s přechodem na sítě 4G a 5G.

## Klíčové vlastnosti

- Implementuje funkci U-LSCF v samostatném síťovém uzlu (Standalone SMLC)
- Poskytuje centralizované řízení polohových služeb pro pool více RNC
- Odděluje vývoj polohovacích funkcí od životního cyklu hardwaru RNC
- Podporuje všechny standardní metody polohování UTRAN (Cell-ID, OTDOA, U-TDOA)
- Využívá standardní rozhraní Iupc pro komunikaci s GMLC Core Network
- Umožňuje flexibilní, škálovatelné nasazení a snadnější správu sítě

## Související pojmy

- [U-LSCF – UTRAN Location System Control Function](/mobilnisite/slovnik/u-lscf/)
- [SAS – Security Attributes Service](/mobilnisite/slovnik/sas/)
- [SMLC – Standalone Mobile Location Center](/mobilnisite/slovnik/smlc/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [U-LSCFS na 3GPP Explorer](https://3gpp-explorer.com/glossary/u-lscfs/)
