---
slug: "flr"
url: "/mobilnisite/slovnik/flr/"
type: "slovnik"
title: "FLR – Frame Loss Ratio"
date: 2025-01-01
abbr: "FLR"
fullName: "Frame Loss Ratio"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/flr/"
summary: "Frame Loss Ratio (FLR) je klíčová metrika kvality služeb (QoS) definovaná 3GPP pro měření podílu ztracených nebo nedoručených datových rámců v multimediální relaci. Je zásadní pro hodnocení a zaručová"
---

FLR je metrika 3GPP pro podíl ztracených nebo nedoručených datových rámců v multimediální relaci, klíčová pro hodnocení kvality služeb v reálném čase, jako je hlas a video.

## Popis

Frame Loss Ratio (FLR) je základní parametr výkonu v rámci architektury kvality služeb (QoS) 3GPP, konkrétně pro třídy konverzačního a streamovacího provozu. Kvantifikuje spolehlivost toku paketových dat výpočtem poměru ztracených rámců k celkovému počtu očekávaných rámců v daném měřicím období. 'Ztracený rámec' je typicky definován jako paket, který nepřijde k příjemci v rámci maximální povolené přenosové doby, nebo jako paket, který sice přijde, ale je natolik poškozený, že jej nelze použít. Tato metrika je nezbytná pro aplikace citlivé na ztrátu paketů, jako je Voice over IP (VoIP), videokonference a živé vysílání, kde ztracené pakety přímo snižují vnímanou kvalitu zvuku/videa.

Z architektonického hlediska se FLR monitoruje end-to-end mezi definovanými měřicími body, často mezi uživatelským zařízením (UE) a partnerskou entitou, jako je mediální server nebo jiné UE. Specifikace 3GPP definují metodiky a protokoly pro měření FLR. Například v IP Multimedia Subsystem (IMS) lze FLR měřit pomocí zpráv řídicího protokolu Real-time Transport Protocol (RTP) (RTCP) vyměňovaných mezi koncovými body. Tyto zprávy obsahují statistiky o odeslaných paketech, ztracených paketech a jitteru, což každému konci umožňuje vypočítat FLR v opačném směru. Síťové prvky jako Policy and Charging Rules Function (PCRF) a Policy and Charging Enforcement Function (PCEF) mohou také používat metriky FLR pro dynamická rozhodnutí o zásadách, jako je úprava charakteristik přenosu nebo spouštění nápravných akcí.

FLR spolupracuje s dalšími parametry QoS, jako je rozpočet zpoždění paketů a míra chybovosti paketů, při definování identifikátoru třídy QoS ([QCI](/mobilnisite/slovnik/qci/)). Každý standardizovaný QCI má přidružené cílové hodnoty těchto parametrů, včetně FLR. Například QCI pro konverzační hlas má velmi nízký rozpočet zpoždění paketů a nízkou cílovou hodnotu FLR, aby byla zajištěna čistá a nepřerušovaná řeč. Síť používá tyto profily QCI k odpovídající prioritizaci provozu, alokaci prostředků a aplikaci mechanismů opravy chyb. Sledování FLR umožňuje operátorům ověřit, že síť plňuje tyto garantované úrovně výkonu, provádět analýzu hlavní příčiny degradace kvality a optimalizovat konfiguraci sítě pro lepší poskytování služeb.

## K čemu slouží

Vytvoření metriky Frame Loss Ratio bylo motivováno přechodem od okruhově přepínaných k paketově přepínaným sítím pro služby komunikace v reálném čase. V tradiční okruhově přepínané telefonii byla kvalita inherentně vysoká a konzistentní díky vyhrazeným kanálům. Paketově přepínané sítě, jako jsou ty založené na IP, však zavádějí proměnlivé zpoždění, jitter a ztrátu paketů kvůli přetížení, změnám směrování a přenosovým chybám. Aby bylo možné komerčně zavádět služby jako VoIP a videotelefonie v těchto sítích, byl nezbytný standardizovaný, objektivní měřítko ztráty dat pro definici, prodej a sledování kvality služeb.

FLR řeší problém kvantifikace degradace služeb způsobem, který přímo koreluje s uživatelským vnímáním. U multimediálních kodeků ztráta paketů vede k mezerám, klikání, zamrznutí snímků videa nebo rozmazaným obrazům. Definováním FLR poskytlo 3GPP společný jazyk pro výrobce zařízení, síťové operátory a poskytovatele služeb, aby mohli specifikovat požadavky na výkon, provádět testy interoperability a implementovat systémy správy QoS. Vyřešilo to omezení předchozích přístupů, které mohly měřit pouze hrubou ztrátu paketů bez zohlednění rámcování na aplikační vrstvě nebo časových omezení klíčových pro média v reálném čase. FLR tvoří základ pro smlouvy o úrovni služeb (SLA), což operátorům umožňuje garantovat určitou úroveň výkonu a poskytuje jasnou metriku pro řešení problémů a péči o zákazníky při výskytu problémů s kvalitou.

## Klíčové vlastnosti

- Standardizovaná metrika QoS pro ztrátu paketů ve službách v reálném čase
- Definována pro každý identifikátor třídy QoS (QCI) s cílovými hodnotami
- Měřena end-to-end mezi koncovými body relace
- Využívá protokoly jako RTCP pro hlášení měření
- Nedílná součást monitorování výkonu a správy sítě
- Používá se pro dynamické řízení zásad a přidělování prostředků

## Související pojmy

- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [FLR na 3GPP Explorer](https://3gpp-explorer.com/glossary/flr/)
