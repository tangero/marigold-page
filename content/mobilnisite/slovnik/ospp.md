---
slug: "ospp"
url: "/mobilnisite/slovnik/ospp/"
type: "slovnik"
title: "OSPP – Operating System Protection Profile"
date: 2025-01-01
abbr: "OSPP"
fullName: "Operating System Protection Profile"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ospp/"
summary: "OSPP je bezpečnostní specifikace v rámci 3GPP, která definuje ochranné profily pro operační systémy používané v síťových zařízeních a zajišťuje jejich soulad s přísnými bezpečnostními požadavky. Řeší"
---

OSPP je bezpečnostní specifikace 3GPP, která definuje ochranné profily pro operační systémy v síťových zařízeních, aby zajistila, že splňují přísné bezpečnostní požadavky a chrání před útoky.

## Popis

Ochranný profil operačního systému (OSPP) je bezpečnostní rámec definovaný 3GPP, konkrétně v technické specifikaci 33.916, jehož cílem je stanovit standardizované ochranné profily pro operační systémy nasazené v telekomunikačních síťových zařízeních. Stanovuje soubor bezpečnostních požadavků a hodnotících kritérií, které musí operační systémy splňovat, aby zmírnily rizika, jako je neoprávněný přístup, malware a zneužití softwarových zranitelností. OSPP funguje v širším kontextu bezpečnostní architektury 3GPP a zaměřuje se na softwarovou vrstvu, která podporuje síťové funkce, včetně virtualizovaných prostředí, jako je virtualizace síťových funkcí ([NFV](/mobilnisite/slovnik/nfv/)), a cloudových (cloud-native) nasazení. Tento profil je založen na společných kritériích pro hodnocení bezpečnosti informačních technologií, která jsou přizpůsobena specifickým potřebám mobilních sítí, kde je klíčová vysoká dostupnost, integrita a důvěrnost.

Z architektonického hlediska OSPP definuje bezpečnostní funkční požadavky (SFR) a požadavky na bezpečnostní záruky (SAR), které pokrývají aspekty, jako je řízení přístupu, auditování, kryptografická podpora a izolace prostředků. Specifikuje, jak by operační systémy měly vynucovat bezpečnostní politiky, spravovat uživatelská oprávnění a chránit před hrozbami, jako je přetečení bufferu nebo zvýšení oprávnění. Mezi klíčové komponenty patří bezpečnostní cíle, které podrobně popisují konkrétní bezpečnostní cíle pro danou implementaci operačního systému, a metodiky hodnocení, které posuzují soulad s profilem. OSPP funguje tak, že poskytuje základnu pro dodavatele, aby mohli navrhovat a certifikovat své operační systémy, a zajistit tak, že obsahují utvrzené konfigurace, zabezpečené procesy zavádění systému (secure boot) a mechanismy správy zranitelností. Tím se snižuje prostor pro útoky v síťových prvcích, jako jsou základnové stanice, servery jádra sítě a systémy správy.

V praxi se OSPP uplatňuje u operačních systémů běžících na hardwaru nebo virtuálních strojích, které hostují síťové funkce definované 3GPP, jako jsou gNodeB v 5G nebo evolved NodeB v 4G. Spolupracuje s dalšími bezpečnostními specifikacemi, například pro ověřování a šifrování, a vytváří tak strategii obrany do hloubky (defense-in-depth). Tím, že ukládá funkce, jako je povinné řízení přístupu (např. prostřednictvím SELinux nebo podobných rámců), zabezpečené postupy aktualizace a schopnosti detekce vniknutí, pomáhá OSPP předcházet narušením, která by mohla vést k výpadkům služeb nebo únikům dat. Jeho role je klíčová v moderních sítích, kde softwarově definovaná infrastruktura zvyšuje vystavení kybernetickým hrozbám, a soulad s OSPP dává operátorům jistotu, že jejich zařízení splňují průmyslem uznávané bezpečnostní standardy.

## K čemu slouží

OSPP byl vytvořen jako reakce na rostoucí kybernetické hrozby cílené na mobilní sítě, zejména když se sítě vyvíjely směrem k softwarovým a virtualizovaným architekturám. Před jeho zavedením operační systémy v síťových zařízeních často postrádaly standardizované bezpečnostní profily, což vedlo k nekonzistentní úrovni ochrany a zranitelnostem, které mohli útočníci zneužít. Rozšíření technologií [NFV](/mobilnisite/slovnik/nfv/) a cloudu ve vydáních 13 a novějších tato rizika prohloubilo, protože tradiční bezpečnostní opatření zaměřená na hardware se pro dynamická softwarová prostředí stala nedostatečná.

Tento profil řeší problémy, jako jsou slabá řízení přístupu, nedostatečné auditní stopy a neopravené softwarové zranitelnosti, které by mohly ohrozit integritu a dostupnost sítě. Definováním společného souboru bezpečnostních požadavků umožňuje OSPP interoperabilitu a důvěru napříč nasazeními od více dodavatelů a zajišťuje, že všechny operační systémy splňují minimální bezpečnostní základ. Historicky byl jeho vývoj motivován případy narušení sítí a potřebou regulatorního souladu v telekomunikacích, což vedlo 3GPP k začlenění robustní softwarové bezpečnosti do svých standardů. OSPP zaplňuje mezeru, kterou zanechaly dřívější specifikace více zaměřené na kryptografickou a síťovou vrstvu zabezpečení, a poskytuje tak holistický přístup k zabezpečení podkladové softwarové platformy.

## Klíčové vlastnosti

- Standardizované bezpečnostní požadavky založené na hodnocení dle společných kritérií (common criteria)
- Ochrana před neoprávněným přístupem a zvýšením oprávnění (privilege escalation)
- Mechanismy povinného řízení přístupu (mandatory access control) a izolace prostředků
- Zabezpečené procesy zavádění systému (secure boot) a aktualizace pro zajištění integrity softwaru
- Schopnosti auditování a monitorování pro detekci hrozeb
- Kompatibilita s virtualizovanými a cloudovými (cloud-native) síťovými funkcemi

## Související pojmy

- [NFV – Network Functions Virtualization](/mobilnisite/slovnik/nfv/)

## Definující specifikace

- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)

---

📖 **Anglický originál a plná specifikace:** [OSPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ospp/)
