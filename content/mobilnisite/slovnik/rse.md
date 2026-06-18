---
slug: "rse"
url: "/mobilnisite/slovnik/rse/"
type: "slovnik"
title: "RSE – Radio System Entity"
date: 2025-01-01
abbr: "RSE"
fullName: "Radio System Entity"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rse/"
summary: "Základní architektonická komponenta v sítích 3GPP představující logickou nebo fyzickou entitu zodpovědnou za rádiový přenos a příjem. Zahrnuje funkční prvky, které spravují vzdušné rozhraní, a tvoří z"
---

RSE je základní architektonická komponenta v sítích 3GPP, která představuje logickou nebo fyzickou entitu zodpovědnou za rádiový přenos, příjem a správu rozhraní k přenosovému médiu (vzdušného rozhraní).

## Popis

Rádiová systémová entita (Radio System Entity, RSE) je klíčový architektonický koncept ve specifikacích 3GPP, který slouží jako základní stavební prvek pro rádiovou přístupovou síť (RAN). Nejde o jediný konkrétní kus hardwaru, ale spíše o logickou entitu, která abstrahuje funkce potřebné pro rádiovou komunikaci. RSE zahrnuje všechny nezbytné schopnosti pro vysílání a příjem rádiových signálů přes vzdušné rozhraní (rozhraní Uu v UMTS/[UTRAN](/mobilnisite/slovnik/utran/), LTE-Uu v [E-UTRAN](/mobilnisite/slovnik/e-utran/) a NR-Uu v NG-RAN). To zahrnuje základní pásmovou (baseband) část, rádiové kmitočtové ([RF](/mobilnisite/slovnik/rf/)) komponenty, antény a přidružený řídicí software, který spravuje procedury fyzické vrstvy, adaptaci spojení a plánování.

Architektonicky RSE představuje bod, kde se digitální síť připojuje k analogovému rádiovému prostředí. V tradičním nasazení makrobuňky může RSE odpovídat kompletní základnové stanici (NodeB v UMTS, eNodeB v LTE nebo gNB v 5G NR). Koncept je však flexibilní a může platit i pro disintegrované RAN architektury. Například v kontextu centralizované RAN (C-RAN) nebo otevřené RAN (O-RAN) může být funkčnost RSE rozdělena mezi distribuovanou jednotku ([DU](/mobilnisite/slovnik/du/)), která zvládá plánování v reálném čase pro vrstvu 1 a vrstvu 2, a rádiovou jednotku ([RU](/mobilnisite/slovnik/ru/)), která zvládá RF vysílání a příjem. RSE, jak je definována ve specifikacích slovníku, zapouzdřuje tuto celistvost rádiové funkčnosti bez ohledu na její fyzickou implementaci.

Role RSE je klíčová pro nasazení, plánování a optimalizaci sítě. Definuje oblast pokrytí (buňku), spravuje rádiové zdroje (čas, kmitočet, výkon, prostorové vrstvy) a provádí klíčové procedury, jako je vyhledávání buňky, náhodný přístup a signalizace předávání spojení. Rozhraní s jádrem sítě (přes rozhraní Iu, S1 nebo [NG](/mobilnisite/slovnik/ng/)) slouží k zřizování přenosových kanálů pro uživatelská data a správě mobility. Standardizovaná definice RSE zajišťuje, že síťová zařízení od různých výrobců mohou vzájemně spolupracovat a poskytovat konzistentní uživatelský zážitek. Jde o základní termín používaný v technických specifikacích, modelech pro dimenzování sítě a při plánování kapacity pro kvantifikaci počtu potřebných rádiových bodů k obsluze dané oblasti a přenosové poptávky.

## K čemu slouží

Rádiová systémová entita (RSE) byla zavedena, aby poskytla standardizovaný, na technologii nezávislý termín pro základní bod rádiového přenosu v síti 3GPP. Před její formální definicí mohly být diskuze o síťové architektuře nejednoznačné a používaly výrobci specifické nebo technologie specifické termíny jako 'základnová stanice' nebo '[BTS](/mobilnisite/slovnik/bts/)', které mohly implikovat odlišný rozsah funkčnosti. Vytvoření RSE mělo za cíl stanovit jasnou a konzistentní slovní zásobu ve specifikacích 3GPP, kterou lze aplikovat napříč různými technologiemi rádiového přístupu, od GSM/[EDGE](/mobilnisite/slovnik/edge/) přes UMTS a LTE až po 5G NR.

Jejím účelem je řešit problém architektonické abstrakce a budoucí odolnosti. Definováním logické entity namísto fyzické skříně zajistilo 3GPP, že základní koncept zůstal platný, i když se hardwarové implementace vyvíjely. Například přechod od integrovaných makro základnových stanic k cloudovým, disintegrovaným RAN s oddělenými centrálními jednotkami (CU), distribuovanými jednotkami (DU) a rádiovými jednotkami (RU) nezneplatnil termín RSE; znamenalo to pouze, že funkčnost RSE byla rozdělena mezi tyto nové fyzické uzly. Tato abstrakce je klíčová pro psaní specifikací, které jsou nezávislé na implementaci, zaměřují se na funkční požadavky a rozhraní namísto vynucování konkrétního hardwarového provedení.

Koncept RSE dále podporuje konzistentní modelování a plánování sítě. Inženýři mohou modelovat síťovou kapacitu a pokrytí na základě schopností a hustoty RSE bez ohledu na podkladovou RAT. Poskytuje společnou jednotku pro diskusi o scénářích nasazení sítě, koordinaci rušení a provozu s více RAT (Multi-Radio Access Technology). RSE v podstatě existuje, aby vytvořila společný jazyk pro architekturu rádiové sítě, umožnila přesnou technickou komunikaci, zjednodušila popisy systémů ve standardech a usnadnila vývoj RAN směrem k flexibilnějším a virtualizovanějším implementacím.

## Klíčové vlastnosti

- Abstrahuje funkce rádiového přenosu a příjmu do logické síťové entity
- Nezávislá na technologii, použitelná pro architektury RAN UMTS, LTE a 5G NR
- Zahrnuje základní pásmovou (baseband) část, RF komponenty a anténní systémy
- Slouží jako základní jednotka pro plánování pokrytí a kapacity sítě
- Vytváří rozhraní s jádrem sítě pro zřizování a správu toků uživatelských dat
- Poskytuje základ pro definici buněk a správu řízení rádiových zdrojů

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [RSE na 3GPP Explorer](https://3gpp-explorer.com/glossary/rse/)
