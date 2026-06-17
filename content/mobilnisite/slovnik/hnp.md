---
slug: "hnp"
url: "/mobilnisite/slovnik/hnp/"
type: "slovnik"
title: "HNP – Home Network Prefix"
date: 2015-01-01
abbr: "HNP"
fullName: "Home Network Prefix"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/hnp/"
summary: "Home Network Prefix (HNP) je síťový prefix přiřazený mobilnímu uzlu v IP mobilních protokolech, jako je DSMIPv6. Slouží jako stabilní, topologicky správná domovská adresa mobilního uzlu, která mu umož"
---

HNP (Home Network Prefix) je domovský síťový prefix přiřazený mobilnímu uzlu v IP mobilních protokolech, který slouží jako jeho stabilní domovská adresa pro udržení spojení při pohybu mezi různými přístupovými sítěmi.

## Popis

Home Network Prefix (HNP) je klíčový identifikátor v protokolech pro správu IP mobility, konkrétně definovaný v kontextu 3GPP pro Dual-Stack Mobile IPv6 (DSMIPv6) a Proxy Mobile IPv6 (PMIPv6). Konceptuálně se jedná o prefix IPv6 (nebo adresu/prefix IPv4 v dual-stack scénářích), který je trvale asociován s mobilním uzlem ([MN](/mobilnisite/slovnik/mn/)) a ukotven u jeho domovského agenta ([HA](/mobilnisite/slovnik/ha/)) v DSMIPv6 nebo u kotvícího bodu lokální mobility ([LMA](/mobilnisite/slovnik/lma/)) v PMIPv6. Tento prefix definuje 'domovskou síť' MN ve smyslu IP směrování. MN z tohoto prefixu konfiguruje jednu nebo více domovských adres (HoA), které zůstávají konstantní bez ohledu na aktuální místo připojení MN k síti.

Během provozu, když MN přechází do navštívené sítě, získá od místního přístupového směrovače dočasnou adresu (CoA). V DSMIPv6 MN tuto CoA sám registruje u svého HA pomocí zprávy Binding Update, čímž vytvoří vazbu mezi svou stabilní HoA (odvozenou od HNP) a aktuální CoA. HA pak zachytává pakety určené pro HoA MN a tuneluje je na CoA MN. V PMIPv6, což je síťový protokol, provádí registraci u LMA jménem MN brána pro přístup k mobilitě ([MAG](/mobilnisite/slovnik/mag/)) v navštívené síti. LMA, který hostuje HNP, zajišťuje směrování paketů k MAG obsluhující MN. HNP je tedy topologickým ukotvovacím bodem pro IP relaci MN, což umožňuje plynulou kontinuitu IP.

Přidělení HNP je základní funkcí domovské sítě. Typicky je přiřazen během počátečního připojení MN nebo zřízení služby. HNP je uložen v profilu předplatného MN v infrastruktuře [AAA](/mobilnisite/slovnik/aaa/) (Authentication, Authorization, and Accounting). Během autentizace přístupu k síti může server AAA sdělit přiřazený HNP síťové entitě fungující jako kotva mobility (HA nebo LMA). Rozsah HNP je globální, což znamená, že je směrovatelný v rámci internetu, což umožňuje komunikujícím uzlům komunikovat s MN pomocí jeho domovské adresy bez jakéhokoli povědomí o jeho mobilitě.

## K čemu slouží

Koncept HNP byl vyvinut k řešení základního problému kontinuity relace pro mobilní zařízení v IP sítích. Původní architektura internetu předpokládala, že koncové body jsou stacionární; IP adresa hosta také označovala jeho topologickou polohu. Mobilita tento předpoklad narušuje, protože přechod do nové sítě obvykle vyžaduje novou IP adresu, což přerušuje existující TCP spojení a relace aplikací. Mobilní IP protokoly (MIPv6, DSMIPv6) byly vytvořeny, aby oddělily identifikátor uzlu (jeho domovskou adresu) od jeho lokátoru (jeho dočasné adresy).

HNP poskytuje stabilní základ identifikátoru pro toto oddělení. Umožňuje mobilnímu uzlu mít trvalý 'domov' na internetu reprezentovaný jeho domovskou adresou odvozenou od HNP. Tím se řeší problém dosažitelnosti a trvání relace. Motivací pro standardizaci HNP v rámci 3GPP bylo poskytnout jednotné, IP-based řešení mobility pro 3GPP a ne-3GPP přístupové sítě (jako Wi-Fi), jak je definováno v Evolved Packet Core (EPC). Umožňuje funkce jako plynulé předávání mezi 3GPP a důvěryhodným ne-3GPP přístupem bez přerušení IP služeb, jako je VoIP nebo video streamování. Předchozí přístupy spoléhaly na mobilitu na linkové vrstvě nebo řešení na aplikační vrstvě, která byla často neefektivní nebo ne univerzálně použitelná.

## Klíčové vlastnosti

- Slouží jako stabilní směrovací prefix pro domovskou adresu mobilního uzlu
- Ukotven u domovského agenta (DSMIPv6) nebo kotvícího bodu lokální mobility (PMIPv6)
- Umožňuje kontinuitu IP relace napříč různými přístupovými sítěmi
- Globálně směrovatelný, umožňující přímou komunikaci od komunikujících uzlů
- Přiřazen z adresního prostoru domovského operátora mobilního uzlu
- Podporuje jak prefixy IPv6, tak adresy/prefixy IPv4 v dual-stack provozu

## Definující specifikace

- **TS 24.327** (Rel-12) — Mobility between I-WLAN and GPRS

---

📖 **Anglický originál a plná specifikace:** [HNP na 3GPP Explorer](https://3gpp-explorer.com/glossary/hnp/)
