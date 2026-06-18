---
slug: "ipa"
url: "/mobilnisite/slovnik/ipa/"
type: "slovnik"
title: "IPA – Inferential Power Analysis"
date: 2025-01-01
abbr: "IPA"
fullName: "Inferential Power Analysis"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ipa/"
summary: "Bezpečnostní testovací metodika používaná k vyhodnocení odolnosti kryptografických implementací, zejména v 3GPP uživatelských zařízeních (UE), proti vedlejším kanálovým útokům využívajícím variace v o"
---

IPA je bezpečnostní testovací metodika používaná k vyhodnocení odolnosti kryptografických implementací v 3GPP uživatelských zařízeních proti vedlejším kanálovým útokům, které využívají variace v odběru elektrického proudu.

## Popis

Inferential Power Analysis (IPA) je sofistikovaná technika vedlejším kanálem a odpovídající hodnotící rámec pro posouzení protiopatření, standardizovaný v rámci 3GPP. Funguje na principu, že okamžitá spotřeba elektrického proudu kryptografického zařízení (jako je [SIM](/mobilnisite/slovnik/sim/) karta nebo bezpečnostní prvek UE) koreluje s interními zpracovávanými daty, například tajnými klíči a mezivýsledky během provádění algoritmu. Statistickou analýzou velkého počtu měření energetických stop (power traces) pořízených při provádění kryptografických operací může útočník odvodit citlivé informace. Specifikace 3GPP TS 35.909 definuje metodiky a požadavky pro testování zranitelnosti implementací univerzální integrované obvodové karty (UICC) a terminálu ([TE](/mobilnisite/slovnik/te/)) vůči takovým útokům, aby byla zajištěna jejich definovaná úroveň odolnosti.

Architektura testování IPA zahrnuje specializované laboratorní vybavení, včetně přesného nastavení pro měření proudu, kontrolovaného testovacího prostředí a softwaru pro sběr a analýzu stop. Testované zařízení ([DUT](/mobilnisite/slovnik/dut/)), například UICC, je stimulováno známými nebo zvolenými vstupy, zatímco je jeho napájecí vedení monitorováno s vysokým časovým rozlišením. Výsledné energetické stopy jsou následně zpracovány pomocí statistických metod, jako je diferenciální analýza spotřeby ([DPA](/mobilnisite/slovnik/dpa/)) nebo korelační analýza spotřeby ([CPA](/mobilnisite/slovnik/cpa/)). Tyto metody porovnávají naměřené stopy s hypotetickými modely spotřeby proudu založenými na odhadech tajného klíče. Významná korelace odhalí správné bity klíče.

Role IPA v bezpečnostním ekosystému 3GPP je proaktivní a obranná. Zatímco popisuje vektor útoku, její standardizace si primárně klade za cíl definovat společnou, přísnou testovací základnu. Výrobci musí prokázat, že jejich implementace neunikají dostatek informací, aby bylo IPA proveditelné v rámci praktických omezení (např. počet stop, čas). To zahrnuje implementaci hardwarových a softwarových protiopatření, jako je vyvažování spotřeby, náhodná zpoždění, maskování mezivýsledků a bezpečné logické styly. Povinným testováním odolnosti vůči IPA zajišťuje 3GPP, že základní kryptografická důvěra v mobilních sítích – chránící identitu uživatele, důvěrnost a integritu – je zachována i proti hrozbám na fyzické vrstvě.

## K čemu slouží

IPA byla zavedena, aby řešila rostoucí hrozbu fyzických vedlejších kanálových útoků proti autentizačním modulům mobilních sítí. Před její standardizací se bezpečnostní hodnocení primárně zaměřovala na logické zranitelnosti a zranitelnosti na úrovni protokolu, za předpokladu 'black-box' modelu, kde byla kryptografická implementace dokonalá. Reálné implementace v hardwaru a firmwaru jsou však nedokonalé a unikají z nich fyzické informace. Vytvoření testovacích standardů IPA bylo motivováno potřebou zvýšit úroveň bezpečnostní záruky pro UICC a terminály nad rámec teoretické síly algoritmu tak, aby zahrnovala i robustnost praktické implementace.

Problém, který řeší, je potenciální kompromitace dlouhodobých klíčů účastníka (jako je Ki v protokolu Authentication and Key Agreement) pomocí neinvazivních a nízkonákladových prostředků. Útočník s fyzickým přístupem k zařízení nebo kartě by teoreticky mohl klíč extrahovat a naklonovat identitu účastníka. Definováním standardizované útočné metodiky a kritérií úspěšnosti/neúspěšnosti umožňuje 3GPP konzistentní a srovnatelná bezpečnostní hodnocení napříč odvětvím. To podporuje přijetí protiopatření již ve fázi návrhu, což v konečném důsledku chrání celou síť před podvodným využíváním služeb a odposlechem pocházejícím z kompromitovaných přihlašovacích údajů. Její zařazení odráží holistický přístup 3GPP k bezpečnosti, který uznává, že řetěz je tak silný jako jeho nejslabší článek, kterým může být často právě fyzické provádění kryptografie.

## Klíčové vlastnosti

- Standardizovaná metodika pro testování odolnosti vůči vedlejším kanálovým útokům
- Zaměření na spotřebu elektrického proudu jako zdroj úniku informací
- Definuje hodnotící kritéria pro implementace UICC a terminálu
- Podporuje statistické analytické techniky jako DPA a CPA
- Podněcuje implementaci hardwarových a softwarových protiopatření
- Poskytuje společnou základnu pro bezpečnostní certifikaci

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [DPA – Differential Power Analysis](/mobilnisite/slovnik/dpa/)

## Definující specifikace

- **TR 35.909** (Rel-19) — 3GPP MILENAGE Algorithm Design Report

---

📖 **Anglický originál a plná specifikace:** [IPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipa/)
