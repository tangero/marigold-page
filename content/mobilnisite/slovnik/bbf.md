---
slug: "bbf"
url: "/mobilnisite/slovnik/bbf/"
type: "slovnik"
title: "BBF – Bearer Binding Function"
date: 2025-01-01
abbr: "BBF"
fullName: "Bearer Binding Function"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bbf/"
summary: "Funkce vázání přenosových kanálů (Bearer Binding Function, BBF) je klíčovou součástí architektury řízení politiky a účtování (PCC) dle 3GPP. Je odpovědná za přiřazení IP toků v rámci toku služebních d"
---

BBF je funkce řízení politiky a účtování (PCC), která váže IP toky ke konkrétnímu přenosovému kanálu (bearer), aby zajistila, že provoz obdrží požadovanou kvalitu služeb napříč přístupovou sítí.

## Popis

Funkce vázání přenosových kanálů (Bearer Binding Function, BBF) je logická funkce uvnitř funkce pravidel politiky a účtování ([PCRF](/mobilnisite/slovnik/pcrf/)) v sítích 3GPP. Jejím hlavním úkolem je provádět 'vázání přenosových kanálů', což je proces mapování IP toků, identifikovaných filtry toku služebních dat, na vhodný přenosový kanál EPS nebo tok QoS, který může doručit požadovanou kvalitu služeb (QoS). Toto mapování je klíčové pro vynucení QoS politik stanovených PCRF napříč celou datovou cestou, od jádra sítě přes rádiovou přístupovou síť až k uživatelskému zařízení (UE). BBF funguje na základě pravidel [PCC](/mobilnisite/slovnik/pcc/) přijatých od funkce rozhodování o politice ([PDF](/mobilnisite/slovnik/pdf/)) v PCRF. Tato pravidla PCC obsahují parametry jako identifikátor třídy QoS ([QCI](/mobilnisite/slovnik/qci/)), prioritu přidělení a udržení ([ARP](/mobilnisite/slovnik/arp/)), garantované a maximální přenosové rychlosti ([GBR](/mobilnisite/slovnik/gbr/)/[MBR](/mobilnisite/slovnik/mbr/)) a šablony toku služebních dat. BBF používá tato pravidla k určení správného přenosového kanálu pro každý IP tok, čímž zajišťuje, že provoz s různými požadavky na QoS (např. hlas, video, datový provoz typu best-effort) je přenášen na samostatných kanálech s odlišnými charakteristikami.

Architektonicky není BBF samostatným síťovým prvkem, ale je integrována jako podfunkce uvnitř PCRF. Komunikuje s dalšími interními funkcemi PCRF a externími síťovými prvky přes standardizovaná rozhraní. Když PCRF učiní rozhodnutí o politice, komponenta BBF vyhodnotí existující přenosové kanály pro relaci účastníka. Zkontroluje, zda existující kanál (jako výchozí nebo vyhrazený kanál) má atributy QoS odpovídající požadavkům nového toku služebních dat. Pokud je shoda nalezena, je IP tok navázán na tento existující kanál. Pokud žádný vhodný kanál neexistuje, BBF spustí zřízení nového vyhrazeného kanálu s přesnými potřebnými parametry QoS. Toto rozhodnutí je následně sděleno funkci vynucení politiky a účtování ([PCEF](/mobilnisite/slovnik/pcef/)) v PGW (ve 4G) nebo SMF/UPF (v 5G) přes rozhraní Gx, resp. N7.

Činnost BBF je dynamická a bere v úvahu kontext relace. Zohledňuje profil předplatného účastníka, probíhající toky služeb, dostupnost síťových zdrojů a politiky operátora. Například hovor VoLTE by vyžadoval vyhrazený kanál s vysokou prioritou QCI pro hlas, na který by BBF navázala tento konkrétní mediální tok. Souběžný provoz prohlížení webu by byl navázán na výchozí kanál typu best-effort. Tato podrobná kontrola je zásadní pro poskytování diferencovaných služeb a umožnění efektivního využití síťových zdrojů. BBF také zpracovává události modifikace a zrušení přenosových kanálů, čímž zajišťuje, že vázání zůstává konzistentní při spouštění a zastavování služeb.

V systémech 5G se koncept vyvíjí, ale zůstává funkčně analogický. Logika BBF uvnitř funkce řízení politiky (PCF) váže toky služebních dat na toky QoS namísto přenosových kanálů EPS. Tok QoS v 5G představuje nejjemnější úroveň diferenciace QoS v jádru 5G sítě. BBF mapuje aplikační provoz na identifikátor toku QoS (QFI) na základě pravidel QoS pro 5G. Rozhodnutí o vázání jsou vynucována SMF a UPF. Tato kontinuita zdůrazňuje trvalou roli BBF jako kritického spojení mezi politikami služeb na vysoké úrovni a mechanismy přeposílání paketů na nízké úrovni, které tyto politiky realizují v sítích 4G i 5G.

## K čemu slouží

Funkce vázání přenosových kanálů (BBF) byla vytvořena k vyřešení základního problému uplatňování podrobných, službě specifických politik kvality služeb (QoS) v paketově přepínané mobilní síti. Před 3GPP Release 7 a kompletní architekturou PCC bylo řízení QoS statičtější a méně vázané na jednotlivé služby. Zavedení IP multimediálních služeb, jako je hlas a video založené na IMS, vyžadovalo dynamický mechanismus, který by zajistil, že tyto citlivé na zpoždění toky dostanou přednost před daty typu best-effort bez ruční konfigurace pro každého účastníka.

BBF řeší omezení spočívající v použití 'univerzálního' přenosového kanálu pro veškerý provoz. Bez ní by všechny IP pakety od uživatele procházely stejným tunelem v rádiové síti a jádru sítě se stejným zacházením, což by znemožňovalo garantovat nízkou latenci a rozkmity vyžadované pro komunikaci v reálném čase. BBF umožňuje síti dynamicky vytvářet na požádání více logických potrubí (přenosových kanálů) s různými profily QoS. To operátorům umožňuje nabízet služby různých úrovní, efektivně řídit zahlcení sítě upřednostňováním kritického provozu a plnit smlouvy o úrovni služeb (SLA) pro podnikové zákazníky nebo konkrétní aplikace.

Historicky byl její vývoj motivován potřebou podporovat IP multimediální subsystém (IMS) a další pokročilé služby ziskově. Vázáním signalizačních a mediálních toků IMS na odpovídajícím způsobem nakonfigurované vyhrazené kanály mohli operátoři zajistit vysokou kvalitu hlasových a video hovorů, což bylo zásadní pro konkurenceschopnost vůči službám s okruhovým přepojováním a později vůči over-the-top aplikacím. BBF se tak jako součást rámce PCC stala základním kamenem pro umožnění příjmově diferencovaných služeb a efektivního řízení síťových zdrojů v éře mobilní komunikace zcela založené na IP.

## Klíčové vlastnosti

- Mapuje IP toky služebních dat na konkrétní přenosové kanály EPS nebo toky QoS v 5G na základě pravidel PCC/pravidel QoS pro 5G
- Dynamicky spouští zřízení, modifikaci a zrušení vyhrazených přenosových kanálů/toků QoS
- Funguje jako nedílná podfunkce uvnitř PCRF (4G) a PCF (5G)
- Při rozhodování o vázání využívá parametry jako QCI, ARP, GBR a MBR
- Zajišťuje konzistentní vynucování QoS od jádra sítě přes RAN až k UE
- Podporuje současné vázání více služebních toků s různými požadavky na QoS na odpovídající přenosové kanály

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)

## Definující specifikace

- **TS 23.139** (Rel-19) — 3GPP-Fixed Broadband Interworking Stage 2
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.716** (Rel-16) — Wireline and Trusted Non-3GPP Access to 5G Core
- **TS 23.839** (Rel-12) — Fixed-Mobile Convergence Architecture Study
- **TS 23.896** (Rel-12) — Policy & Charging Control for Fixed Broadband Convergence
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [BBF na 3GPP Explorer](https://3gpp-explorer.com/glossary/bbf/)
