---
slug: "ace"
url: "/mobilnisite/slovnik/ace/"
type: "slovnik"
title: "ACE – Authentication and Authorization for Constrained Environments"
date: 2025-01-01
abbr: "ACE"
fullName: "Authentication and Authorization for Constrained Environments"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ace/"
summary: "ACE je bezpečnostní rámec 3GPP pro ověřování a autorizaci zařízení v prostředích s omezenými prostředky, jako je IoT. Umožňuje zabezpečený, odlehčený přístup k síťovým službám pro zařízení s omezeným"
---

ACE je bezpečnostní rámec 3GPP pro ověřování a autorizaci zařízení s omezenými prostředky, jako jsou zařízení IoT, který umožňuje jejich zabezpečený a odlehčený přístup k síťovým službám.

## Popis

Authentication and Authorization for Constrained Environments (ACE) je bezpečnostní rámec standardizovaný 3GPP, který řeší specifické výzvy zabezpečení zařízení s omezenými výpočetními zdroji, jako jsou zařízení v masivní komunikaci typu stroj-stroj (mMTC) a scénářích internetu věcí (IoT). Poskytuje standardizovanou metodu, pomocí které se tato zařízení s omezenými prostředky mohou ověřit v síti a získat autorizaci pro přístup ke konkrétním službám nebo zdrojům. Rámec je navržen jako odlehčený, minimalizuje signalizační režii a nároky na zpracování, aby šetřil životnost baterie a snižoval složitost u nízkonákladových zařízení.

Z architektonického hlediska ACE funguje v rámci bezpečnostní architektury 3GPP, často komunikuje s funkcemi jádra sítě, jako je Authentication Server Function (AUSF) a Network Exposure Function (NEF). Definuje protokoly a procedury pro inicializaci bezpečnostních kontextů a správu autorizačních tokenů. Klíčovou součástí je použití efektivních kryptografických sad a mechanismů autorizace založených na tokenech, jako jsou ty založené na rámci OAuth 2.0 přizpůsobeném pro prostředí s omezenými prostředky (jako ACE-OAuth). To umožňuje zařízení předložit kompaktní, ověřitelný token serveru zdrojů (např. aplikačnímu serveru) k prokázání autorizace pro konkrétní akci, aniž by muselo provádět složité ověřování při každé transakci.

Jak to funguje, zahrnuje několik kroků. Nejprve zařízení s omezenými prostředky (klient) a síť navážou počáteční bezpečnostní asociaci, která může využívat přihlašovací údaje předzřízené na zařízení nebo odvozené z předplatného. Zařízení následně požádá autorizační server v ekosystému 3GPP o přístupový token. Tento token je vázán na konkrétní oprávnění (rozsahy) a je kryptograficky chráněn. Zařízení tento token předloží při přístupu k chráněnému zdroji. Server zdrojů před udělením přístupu ověří integritu tokenu a oprávnění klienta. Tento tok založený na tokenech snižuje potřebu, aby zařízení s omezenými prostředky ukládalo složité stavy relací nebo opakovaně provádělo náročné kryptografické operace.

Úloha ACE v síti spočívá v umožnění škálovatelného a bezpečného přístupu ke službám pro miliardy IoT zařízení. Integruje se s primárními procedurami ověřování a dohodou klíčů 3GPP, ale přidává vrstvu optimalizovanou pro autorizaci v komunikaci na úrovni služeb. Oddělením ověřování (prokázání identity) od autorizace (udělení oprávnění) umožňuje flexibilní uplatňování politik. Je zvláště důležitý pro umožnění zabezpečené komunikace od IoT zařízení k aplikačním serverům hostovaným mimo bezprostřední doménu důvěry operátora, což usnadňuje aplikace vertikálních odvětví.

## K čemu slouží

ACE byl vytvořen, aby vyřešil bezpečnostní výzvy spojené s připojením obrovského počtu IoT zařízení s omezenými prostředky k sítím 3GPP. Tradiční procedury ověřování a dohody klíčů 3GPP, ačkoli robustní pro chytré telefony, jsou často příliš náročné pro jednoduché senzory nebo akční členy s omezenou baterií, pamětí a výpočetním výkonem. Signalizační režie a výpočetní náročnost plných AKA procedur by mohly rychle vybít baterie zařízení a zvýšit zatížení sítě, což by bez optimalizace učinilo masivní nasazení IoT ekonomicky a technicky neproveditelná.

Historický kontext představuje zaměření 3GPP na Cellular IoT (CIoT) počínaje Release 13, s technologiemi jako NB-IoT a LTE-M. Tyto rádiové technologie byly optimalizovány pro nízký příkon a širokopásmové pokrytí, ale odpovídající optimalizace byla potřebná na bezpečnostní a servisní vrstvě. Předchozí přístupy buď aplikovaly plný bezpečnostní model uživatelského zařízení (UE), který byl neefektivní, nebo spoléhaly na nestandardizovaná proprietární bezpečnostní řešení, která bránila interoperabilitě a škálovatelnosti napříč různými výrobci zařízení a síťovými operátory.

ACE byl proto zaveden, aby poskytl standardizovaný, odlehčený rámec pro ověřování a autorizaci přizpůsobený prostředím s omezenými prostředky. Řeší problém umožnění silné bezpečnosti bez uvalení nepřiměřených nákladů na zdroje zařízení. To umožňuje síťovým operátorům a vertikálním odvětvím nasazovat zabezpečená, škálovatelná IoT řešení s důvěrou, neboť vědí, že ověřování zařízení a autorizace služeb jsou řešeny efektivně a v souladu se standardy 3GPP.

## Klíčové vlastnosti

- Odlehčená autorizace založená na tokenech (např. ACE-OAuth) pro klienty s omezenými prostředky
- Podpora efektivních kryptografických sad vhodných pro zařízení s nízkou spotřebou
- Integrace s bezpečnostním rámcem 3GPP a AUSF
- Schopnost delegované autorizace, kdy autorizační server vydává tokeny
- Snížená signalizační režie ve srovnání s plnou AKA pro přístup ke službám
- Vázání přístupových tokenů na konkrétní přihlašovací údaje klienta a oprávnění (rozsahy)

## Definující specifikace

- **TS 24.334** (Rel-19) — ProSe Protocols and Procedures
- **TS 24.547** (Rel-19) — SEAL Identity Management Protocol
- **TS 29.343** (Rel-19) — PC2 Reference Point Stage 3 Specification
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [ACE na 3GPP Explorer](https://3gpp-explorer.com/glossary/ace/)
