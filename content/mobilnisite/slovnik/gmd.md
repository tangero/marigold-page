---
slug: "gmd"
url: "/mobilnisite/slovnik/gmd/"
type: "slovnik"
title: "GMD – Group Message Delivery"
date: 2025-01-01
abbr: "GMD"
fullName: "Group Message Delivery"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gmd/"
summary: "Servisní schopnost, která umožňuje efektivní doručování zpráv skupině uživatelů nebo zařízení. Optimalizuje síťové prostředky využitím skupinové adresace a doručovacích mechanismů a podporuje aplikace"
---

GMD je servisní schopnost, která umožňuje efektivní doručování zpráv skupině uživatelů nebo zařízení pomocí skupinové adresace za účelem optimalizace síťových prostředků.

## Popis

Group Message Delivery (GMD) je síťová servisní schopnost, která usnadňuje efektivní rozesílání zpráv definované skupině příjemců, jako jsou uživatelská zařízení (UE) nebo IoT zařízení. Na rozdíl od individuálního doručování zpráv, které vyžaduje samostatnou transakci pro každého příjemce, GMD využívá skupinovou adresaci ke snížení signalizační režie a optimalizaci využití prostředků v jádrové síti i v rádiové přístupové síti. Typicky je implementována v rámci architektur Service Capability Exposure Function (SCEF) nebo aplikačního serveru, přičemž spolupracuje s funkcemi jádrové sítě, jako je [HSS](/mobilnisite/slovnik/hss/) pro řešení členství ve skupině a [MME](/mobilnisite/slovnik/mme/)/SGSN pro spouštění doručení. Služba zpracovává jak mobilně-terminované, tak aplikací spouštěné zprávy a zajišťuje spolehlivé doručení členům skupiny bez ohledu na jejich stav připojení pomocí mechanismů, jako je odložené doručení.

Z architektonického hlediska GMD funguje tak, že definuje identifikátor skupiny, který reprezentuje cílovou množinu příjemců. Když aplikace nebo síťová funkce zahájí skupinovou zprávu, schopnost GMD převede tento identifikátor skupiny na seznam individuálních identifikátorů účastníků (např. [IMSI](/mobilnisite/slovnik/imsi/) nebo [MSISDN](/mobilnisite/slovnik/msisdn/)) dotazem na úložiště členství ve skupinách. Poté řídí proces doručení, který může zahrnovat rozhraní s centrem služby krátkých zpráv (SMSC) pro doručování založené na SMS nebo použití IP mechanismů jako [HTTP](/mobilnisite/slovnik/http/)/2 pro datové zprávy. Pro scénáře IoT se GMD často integruje s SCEF, aby poskytovala síťová [API](/mobilnisite/slovnik/api/) pro aplikační servery, což jim umožňuje požadovat skupinové doručování zpráv bez nutnosti přímého přístupu k rozhraním jádrové sítě.

Pracovní postup zahrnuje několik klíčových komponent: samotnou službu GMD, databáze pro správu skupin a doručovací brány. Po přijetí žádosti o doručení služba GMD ověří identitu žadatele a autorizaci skupiny. Následně určí optimální způsob doručení na základě typu zprávy, schopností příjemců a stavu sítě. Například pro ne-reálné aktualizace IoT zařízení může použít doručování na pozadí se síťovým spouštěním pro probuzení zařízení v režimu úspory energie. Služba také implementuje hlášení o doručení a zpracování chyb, čímž poskytuje zpětnou vazbu původci o úspěšném nebo neúspěšném doručení zprávy členům skupiny. Tím je zajištěna odpovědnost a umožněny mechanismy opakování v případě dočasných selhání.

## K čemu slouží

GMD bylo zavedeno, aby řešilo neefektivnost hromadného doručování zpráv v celulárních sítích, zejména s exponenciálním růstem IoT a komunikací typu stroj-stroj ve verzi 15 (Release 15). Tradiční metody doručování zpráv, jako jsou individuální SMS nebo IP pakety pro každého příjemce, generovaly při škálování na tisíce či miliony zařízení nadměrný signalizační provoz a zatížení jádrové sítě, což vedlo k přetížení a zhoršení výkonu pro ostatní služby. To bylo kritickým omezením pro případy užití, jako jsou aktualizace firmwaru pro IoT zařízení, vysílání nouzových výstrah nebo zprávy velení a řízení pro týmy klíčových misí.

Vytvoření GMD poskytuje standardizovaný, síťově optimalizovaný mechanismus pro skupinově orientované zasílání zpráv. Řeší problém škálovatelného rozesílání zpráv zavedením skupinové adresace, která umožňuje, aby jediná transakce zprávy z aplikační vrstvy byla sítí efektivně rozdistribuována více příjemcům. To ve srovnání se sekvenčním jednosměrným doručováním snižuje latenci, signalizační režii a spotřebu prostředků. Také umožňuje nové servisní modely, kde aplikace nemusí spravovat individuální adresy zařízení, což zjednodušuje aplikační logiku.

Historicky bylo skupinové zasílání zpráv často implementováno na aplikační vrstvě bez povědomí sítě, což vedlo k neoptimálnímu využití rádiové a jádrové sítě. GMD jako síťová schopnost umožňuje operátorům řídit a optimalizovat proces doručení. Podporuje funkce jako optimalizace času doručení, zpracování priority a integraci se službami síťového spouštění pro IoT zařízení v nečinném režimu. To je obzvláště důležité pro nasazení 5G a massive IoT, kde je efektivní skupinová komunikace klíčová pro správu velkých flotil zařízení v chytrých městech, průmyslové automatizaci a systémech veřejného varování.

## Klíčové vlastnosti

- Používá skupinovou adresaci ke snížení signalizační režie při hromadném doručování zpráv
- Integruje se s SCEF pro API přístup aplikačních serverů
- Podporuje mechanismy doručování zpráv jak prostřednictvím SMS, tak na bázi IP
- Poskytuje hlášení o doručení a zpracování chyb pro pokusy o skupinové doručení
- Umožňuje odložené doručení pro offline nebo nečinná zařízení
- Optimalizuje využití prostředků v jádrové a rádiové síti prostřednictvím hromadného zpracování

## Související pojmy

- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)

## Definující specifikace

- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs

---

📖 **Anglický originál a plná specifikace:** [GMD na 3GPP Explorer](https://3gpp-explorer.com/glossary/gmd/)
