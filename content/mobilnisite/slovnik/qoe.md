---
slug: "qoe"
url: "/mobilnisite/slovnik/qoe/"
type: "slovnik"
title: "QoE – Quality of Experience"
date: 2025-01-01
abbr: "QoE"
fullName: "Quality of Experience"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/qoe/"
summary: "Quality of Experience (QoE, Kvalita uživatelského zážitku) je uživatelsky orientovaná míra celkové přijatelnosti aplikace nebo služby z pohledu koncového uživatele. Kvantifikuje subjektivní spokojenos"
---

QoE je uživatelsky orientovaná míra celkové přijatelnosti služby, která kvantifikuje subjektivní spokojenost na základě faktorů jako kvalita videa a čistota zvuku.

## Popis

Quality of Experience (QoE, Kvalita uživatelského zážitku) je holistická, uživatelsky orientovaná metrika definovaná 3GPP pro hodnocení vnímané kvality multimediálních služeb, jako je hlas, streamování videa nebo imerzivní aplikace. Na rozdíl od Quality of Service (QoS), která se zaměřuje na objektivní parametry výkonu sítě (např. latenci, ztrátu paketů), QoE kvantifikuje subjektivní spokojenost koncového uživatele. Je ovlivněna složitou souhrou technických faktorů (např. kódování média, stav sítě, schopnosti zařízení) a lidských faktorů (např. očekávání uživatele, kontext použití). Ve standardech 3GPP je QoE modelována pomocí klíčových ukazatelů kvality ([KQI](/mobilnisite/slovnik/kqi/)), které mapují měřitelné parametry na síťové a aplikační vrstvě na předpokládané skóre uživatelského vnímání, často za použití standardizovaných modelů jako Mean Opinion Score ([MOS](/mobilnisite/slovnik/mos/)) pro hlas nebo modely kvality videa.

Z architektonického hlediska jsou měření a správa QoE integrovány do systému 5G prostřednictvím Service Based Architecture ([SBA](/mobilnisite/slovnik/sba/)). Mezi klíčové funkční prvky patří Application Function ([AF](/mobilnisite/slovnik/af/)), která může vyžádat sběr měření QoE pro konkrétní mediální toky, a funkce 5G Core Network jako Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), které vynucují politiky na základě požadavků na QoE. Sběr měření může být prováděn uživatelským zařízením (UE), aplikačním serverem nebo uvnitř samotné sítě (např. prostřednictvím Traffic Detection Function). Nasbírané metriky QoE jsou následně hlášeny AF nebo vyhrazenému analytickému serveru QoE pro monitorování a optimalizaci.

Role QoE v síti je mnohostranná. Umožňuje optimalizaci v uzavřené smyčce, kde síť může dynamicky upravovat přidělování prostředků, rozhodování o předávání hovoru nebo datový tok aplikace na základě zpětné vazby o uživatelském zážitku v reálném čase. Například pokud QoE pro video stream klesne kvůli přetížení, síť může aktivovat politiku ke zvýšení priority QoS toku nebo dát aplikaci pokyn k přepnutí na stream s nižším rozlišením. Tato optimalizace s ohledem na uživatele je klíčová pro zajištění konzistentní kvality služeb v heterogenních síťových prostředích a je základním kamenem pokročilých služeb, jako je síťové dělení (network slicing), kde lze řez přizpůsobit tak, aby garantoval konkrétní úroveň QoE pro prémiové zákazníky nebo kritické aplikace.

## K čemu slouží

Vytvoření standardizovaných rámců QoE v rámci 3GPP bylo motivováno přechodem od hlasově orientované komunikace k mobilnímu provozu dominovanému multimédii a videem. Tradiční parametry QoS se samy o sobě ukázaly jako nedostatečné pro zaručení spokojenosti uživatele, protože přímo nepřekládají do vnímané kvality. Síť mohla doručovat vynikající poměry doručení paketů a nízkou latenci, ale uživatel přesto mohl zažívat špatnou kvalitu videa kvůli agresivní kompresi videa nebo nevhodnému výběru kodeku. QoE tuto mezeru zaplňuje tím, že poskytuje standardizovaný, měřitelný vztah mezi výkonem sítě a skutečným lidským zážitkem.

Historicky se poskytovatelé služeb spoléhali na stížnosti zákazníků nebo široká průzkumy pro odhad spokojenosti, které byly reaktivní a nepřesné. Zavedení QoE v 3GPP, zejména od vydání Release 16, poskytlo proaktivní, technickou metodologii pro kvantifikaci zážitku. Vyřešilo problém optimalizace sítí pro skutečný výsledek služby, nikoli pouze pro mezilehlé přenosové metriky. To bylo obzvláště kritické s příchodem 5G a jeho sliby v podobě rozšířené mobilní širokopásmové komunikace (eMBB), ultra-spolehlivé komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a masivního IoT, z nichž každá má odlišné požadavky na zážitek, které čistá QoS nedokázala adekvátně definovat ani zaručit.

Navíc QoE umožňuje nové obchodní modely a diferenciaci služeb. Operátoři mohou nabízet smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) založené na garantovaných úrovních QoE, nikoli pouze na dostupnosti sítě. Poskytuje také podrobná data potřebná pro inteligentní automatizaci sítě a optimalizaci řízenou umělou inteligencí, což umožňuje sítím samoléčbu a samooptimalizaci na základě trendů v uživatelském zážitku, což v konečném důsledku snižuje provozní náklady a míru odchodů zákazníků a zároveň zvyšuje výnosový potenciál z prémiových služeb.

## Klíčové vlastnosti

- Uživatelsky orientované měření založené na percepčních modelech (např. POLQA pro hlas, VMAF pro video)
- Integrace s rámcem pro řízení politik (Policy Control Framework) 5G pro dynamické úpravy QoS
- Podpora sběru měření v síti, na klientovi a na serveru
- Standardizovaná reportovací rozhraní (např. Nnef_EventExposure, Naf_EventExposure)
- Korelace klíčových ukazatelů kvality (KQI) aplikační vrstvy s parametry QoS transportní vrstvy
- Umožňuje zajištění služeb v uzavřené smyčce a automatizovanou optimalizaci sítě

## Definující specifikace

- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 26.348** (Rel-19) — xMB Interface Specification

---

📖 **Anglický originál a plná specifikace:** [QoE na 3GPP Explorer](https://3gpp-explorer.com/glossary/qoe/)
